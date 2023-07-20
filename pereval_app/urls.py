from django.urls import path
from .views import SubmitData

urlpatterns = [
    path('api/v1/submitData/', SubmitData.as_view(), name='submitData'),
]