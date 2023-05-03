from django.urls import path
from . import views
from views import upload_image

urlpatterns = [
    path('', views.index, name='index'),
    
    path('/upload_image/', upload_image, name='upload_image'),
]

