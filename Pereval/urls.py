from django.contrib import admin
from django.urls import path, include
from pereval_app.views import SubmitData, SubmitDataDetailView
from .yasg import urlpatterns as doc_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('submitData/', SubmitData.as_view()),
    path('submitData/<int:pk>/', SubmitDataDetailView.as_view()),

]

urlpatterns += doc_urls