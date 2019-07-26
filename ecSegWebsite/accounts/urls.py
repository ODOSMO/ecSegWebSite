from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.ecSeg.as_view(), name='ecSeg'),
    path('home/', views.home.as_view(), name='home'),
]
