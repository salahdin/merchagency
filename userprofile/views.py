from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from . forms import *
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
    else:
        form = SignUpForm()
    return render(request, "accounts/user_login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:frontpage')


def frontpage(request):
    if request.method == 'POST':
        print("psto")
        if 'signupform' in request.POST:
            signupform = SignUpForm(data=request.POST)
            print("psto")
            '''addressform = UserAddressForm(data=request.POST)
            profileform = UserProfileForm(data=request.POST)'''
            signinform = SignInForm()
            if signupform.is_valid():
                print("psto")
                username = signupform.cleaned_data['username']
                password = signupform.cleaned_data['password1']
                signupform.save()
                user = authenticate(username=username, password=password)
                # log the user in
                login(request, user)
                messages.success(request, 'Account created successfully')
                return redirect('core:register_service')
            else:
                messages.warning(request, 'Failed to create account')
        else:
            signinform = SignInForm(data=request.POST)
            signupform = SignUpForm()
            if signinform.is_valid():
                print('login1')
                username = signinform.cleaned_data['username']
                password = signinform.cleaned_data['password']
                user = authenticate(username=username, password=password)
                login(request, user)
                print('login2')
                return redirect('core:list_view')
    else:
        signupform = SignUpForm()
        signinform = SignInForm()
    context = {'signupform': signupform,
               'signinform': signinform,
               }
    return render(request, 'accounts/loginpage.html', context)


def editprofile(request):
    if request.method =="POST":
        addressform = UserAddressForm(data=request.POST)
        profileform = UserProfileForm(data=request.POST)
        if addressform.is_valid() and profileform.is_valid():
            address = addressform.save(commit=False)
            profile = profileform.save(commit=False)
            address.user = request.user
            profile.user = request.user
            profile.save()
            address.save()
            return redirect("core:list_view")
    else:
        addressform = UserAddressForm()
        profileform = UserProfileForm()
    return render(request, 'accounts/editprofile.html', {"addressform":addressform, "profileform": profileform})



def profileDetailView(request, id_):

    person = get_object_or_404(User, id=id_)
    profile = UserProfile.objects.get(user=person)
    address = person.useraddress.all()

    return render(request, 'myposts.html', {'person': person, 'profile': profile, 'address': address})
