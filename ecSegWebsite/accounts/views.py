from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout , login
from django.core.files.storage import FileSystemStorage

from django.shortcuts import render
from django.views.generic import TemplateView

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ecSeg(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home/')
    template_name = 'ecSeg.html'

class home(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home/')
    template_name = 'home.html'

def logout_view(request):
    logout(request)

def fileUpload(request):
    if request.method=='POST':
        uploaded_file= request.FILES['document']
        fs = FileSystemStorage(location='/media/images')
        fs.save(uploaded_file.name, uploaded_file)
    return render(request,'fileUpload.html')
