from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from . forms import *
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def frontpage(request):
    if request.method == 'POST':
        if 'signupform' in request.POST:
            signupform = SignUpForm(data=request.POST)
            signinform = SignInForm()

            if signupform.is_valid():
                username = signupform.cleaned_data['username']
                password = signupform.cleaned_data['password1']
                signupform.save()
                user = authenticate(username=username, password=password)
                # log the user in
                login(request, user)
        else:
            signinform = SignInForm(data=request.POST)
            signupform = SignUpForm()

            if signinform.is_valid():
                login(request, signinform.get_user())
    else:
        signupform = SignUpForm()
        signinform = SignInForm()

    return render(request, 'accounts/login.html', {'signupform': signupform, 'signinform': signinform})


def profileDetailView(request, id_):
    if request.user.is_authenticated:
        person = get_object_or_404(User, id=id_)
        person_profile = person.userprofile

        return render(request, 'profileview.html', {'person': person, 'person_profile': person_profile})
    return redirect('/')



def follow(request, id_):
    """
    follow a user or service
    :param request:
    :param id_:
    :return:
    """
    pass