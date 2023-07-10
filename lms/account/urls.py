from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from .views import SignUpView
from . import views

urlpatterns=[
    path('signup/',SignUpView.as_view(),name='signup'),
    re_path(r'^login/$', auth_views.LoginView.as_view(), name="login"),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),

]