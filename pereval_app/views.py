from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from .models import PerevalAdded
from .serializers import PerevalSerializer, DetailedPerevalSerializer
from rest_framework import serializers
from rest_framework import filters

class SubmitData(ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        queryset = super().get_queryset()
        user_email = self.request.query_params.get('user__email')
        if user_email:
            queryset = queryset.filter(user__email=user_email)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = PerevalSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            data = {
                'message': f'Записей с электронной почтой {self.request.query_params.get("user__email")} не найдено!'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Запись успешно создана',
                'id': serializer.data['id'],
            })
        if status.HTTP_400_BAD_REQUEST:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': serializer.errors,
                'id': None,
            })
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': serializer.errors,
                'id': None,
            })


class SubmitDataDetailView(RetrieveAPIView, UpdateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = DetailedPerevalSerializer

    def get(self, request, *args, **kwargs):
        try:
            submission_id = kwargs['pk']
            submission = PerevalAdded.objects.get(id=submission_id)
            serializer = DetailedPerevalSerializer(submission)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PerevalAdded.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Запись не найдена',
            })
        except Exception as e:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': str(e),
            })

    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == 'new':
            serializer = self.get_serializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                data_user = request.data.get('user')
                if data_user is not None:
                    instance_user = pereval.user
                    validating_user_fields = [
                        instance_user.fam != data_user.get('fam'),
                        instance_user.name != data_user.get('name'),
                        instance_user.otc != data_user.get('otc'),
                        instance_user.phone != data_user.get('phone'),
                        instance_user.email != data_user.get('email'),
                    ]
                    if any(validating_user_fields):
                        raise serializers.ValidationError(
                            {'Не удалось обновить запись': 'Нельзя изменять данные пользователя'})
                serializer.save()
                return Response({
                    'state': '1',
                    'message': 'Запись успешно изменена!'
                })
            else:
                return Response({
                    'state': '0',
                    'message': serializer.errors
                })
        else:
            return Response({
                'state': '0',
                'message': f"Не удалось обновить запись: статус записи - {pereval.get_status_display()}!"
            })