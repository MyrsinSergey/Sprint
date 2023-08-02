from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pereval_app.views import SubmitData, EmailAPIView
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register('', SubmitData)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('submitData/', include(router.urls)),
    path('submitData/user__email=<email>', EmailAPIView.as_view()),
]

urlpatterns += doc_urls