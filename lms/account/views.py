from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def profile(request):
    args={'user':request.user}
    return render(request,'myprofile.html',args)

def edit_profile(request):
    if request.method== 'POST':
        form=EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'edit_profile.html',args)

def change_password(request):
    if request.method== 'POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
        else:
            return redirect('change_password')
    else:
        form=PasswordChangeForm(user=request.user)
    args={'form':form}
    return render(request,'change_password.html',args)