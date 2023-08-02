from django.urls import path, include
from rest_framework import routers
from .views import SubmitData, EmailAPIView
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register('', SubmitData)

urlpatterns = [
    path('submitData/', include(router.urls)),
    path('submitData/user__email=<str:email>', EmailAPIView.as_view()),
]

urlpatterns += doc_urls