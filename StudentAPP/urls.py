from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student', views.student),
    path('signin', views.signin),
    path('signup', views.signup),
]