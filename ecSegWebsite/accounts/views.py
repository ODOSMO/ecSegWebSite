from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
import requests
from django.shortcuts import render

from subprocess import run, PIPE
import sys

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

def button(request):
    return render(request, 'button.html')

def output(request):
    data = requests.get("https://www.heroku.com/")
    print(data.text)
    data = data.text
    return render(request, 'button.html', {'data': data})

def external(request):
    inp= request.POST.get('param')
    out=run(sys.executable, ['/Users/Jaureguy/PycharmProjects/ecSegWebSiteRecent/ecSegWebsite/accounts/tests.py',inp ], shell =False,stdout=PIPE)
    print(out.stdout)
    return render(request,'button.html', {'data1': out.stdout})

