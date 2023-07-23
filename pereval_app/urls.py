from django.urls import path
from .views import SubmitData, PerevalDetailView

urlpatterns = [
    path('api/v1/submitData/', SubmitData.as_view(), name='submitData'),
    path('api/v1/submitData/<int:id>/', PerevalDetailView.as_view(), name='pereval-detail'),
]