from django.http import JsonResponse
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView
from .models import PerevalAdded
from .serializers import PerevalSerializer, PerevalDetailSerializer


class SubmitData(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer

    """Создание объекта перевала"""
    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)

        """Результаты метода: JSON"""
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

    """Изменение объекта перевала по id (кроме полей с данными пользователя)"""

    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == 'new':
            serializer = PerevalSerializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'state': '1',
                    'message': 'Запись успешно изменена'
                })
            else:
                return Response({
                    'state': '0',
                    'message': serializer.errors
                })
        else:
            return Response({
                'state': '0',
                'message': f"Не удалось обновить запись: статус записи - {pereval.get_status_display()}"
            })


"""GET запрос для вывода всех записей по email пользователя"""
class EmailAPIView(ListAPIView):
    serializer_class = PerevalDetailSerializer

    def get(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        if PerevalAdded.objects.filter(user__email=email):
            data = PerevalDetailSerializer(PerevalAdded.objects.filter(user__email=email), many=True).data
        else:
            data = {
                'message': f'Записи с электронной почтой {email} не найдены!'
            }
        return JsonResponse(data, safe=False)