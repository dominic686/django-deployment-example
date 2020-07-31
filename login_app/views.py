from django.shortcuts import render
from login_app.form import UserForm, UserProfileInfo

#login requirment
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(req):
    return render(req,'login_app/index.html')

def about_us(req):
    return render(req,'login_app/about_us.html')

def user_login(req):
    if(req.method == 'POST'):
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(req,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('This accout is not active')
        else:
            print("Fail to login")
            print("Username:{}, Password{} might be wrong",format(username,password))
            return HttpResponse('Login fail')
    else:
        return render(req,'login_app/login.html',{})



def register(req):
    registered = False

    if(req.method == 'POST'):
        user_form = UserForm(data=req.POST)
        profile_form = UserProfileInfo(data=req.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in req.FILES:
                profile.profile_pic = req.FILES['profile_pic']

            profile.save()
            registered = True
            print("registered")
    else:
        user_form = UserForm()
        profile_form = UserProfileInfo()

    return render(req,'login_app/register.html',{'user_form':user_form,
                                                 'profile_form':profile_form,
                                                 'registered':registered})

@login_required
def home(req):
    return render(req,'login_app/home.html')

@login_required
def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('index'))
