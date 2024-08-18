from django.urls import path, include
from ProjetoCertificadoPdf.geradoPdf.gpdf.views import Index

urlpatterns = [
    path('', Index.as_view(), name ='index'),
]