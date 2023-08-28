from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'greenpalace'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.Signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='greenpalace/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='greenpalace/logout.hml'), name='logout'),
]
