from rest_framework import generics, status
from rest_framework.response import Response
from .models import PerevalAdded
from .serializers import PerevalSerializer


class SubmitData(generics.GenericAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer

    def post(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)

        if serializer.is_valid():
            obj = serializer.save()
            return Response({f'status': status.HTTP_201_CREATED, 'message': 'Запись успешно создана', 'id': obj.id})
        if status.HTTP_400_BAD_REQUEST:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': serializer.errors})


class PerevalDetailView(generics.RetrieveAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer
    lookup_field = 'id'