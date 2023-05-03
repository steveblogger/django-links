from django.shortcuts import render
from .forms import MyImageForm
from .models import MyImage
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
import pyrebase


# Remember the code we copied from Firebase.
# This can be copied by clicking on the settings icon > project settings, then scroll down in your firebase dashboard
config = {
    "apiKey": "AIzaSyCf9FFFBTzJMJVrAj3KtljPW_qsncfwXg0",
    "authDomain": "mega-links-99a6e.firebaseapp.com",
    "projectId": "mega-links-99a6e",
    "storageBucket": "mega-links-99a6e.appspot.com",
    "messagingSenderId": "614998882612",
    "appId": "1:614998882612:web:98c97da3b30e0864784d61",
    "measurementId": "G-C5V2SLFP1W"
}


def index(request):
    image_list = MyImage.objects.all()
    paginator = Paginator(image_list, 1)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    return render(request, './image_list_admin.html', {'images': images})


@user_passes_test(lambda u: u.is_staff)
def upload_image(request):
    if request.method == 'POST':
        form = MyImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = MyImageForm()
    else:
        form = MyImageForm()
    return render(request, 'upload_image.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def image_list_admin(request):
    image_list = MyImage.objects.all()
    paginator = Paginator(image_list, 1)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    return render(request, './image_list_admin.html', {'images': images})


def image_list(request):
    image_list = MyImage.objects.all()
    paginator = Paginator(image_list, 1)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    return render(request, './image_list.html', {'images': images})


def delete_image(request, uid):
    image = get_object_or_404(MyImage, id=uid)
    if request.method == 'POST':
        image.delete()
        return redirect('image_list_admin')
    return render(request, 'delete_image.html', {'image': image})
