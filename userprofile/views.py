from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from . forms import *
from django.contrib.auth.models import User


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
    return redirect('/')


def frontpage(request):
    if request.method == 'POST':
        if 'signupform' in request.POST:
            signupform = SignUpForm(data=request.POST)
            addressform = UserAddressForm(data=request.POST)
            profileform = UserProfileForm(data=request.POST)
            signinform = SignInForm()

            if signupform.is_valid():
                username = signupform.cleaned_data['username']
                password = signupform.cleaned_data['password1']
                signupform.save()
                user = authenticate(username=username, password=password)
                # log the user in
                address = addressform.save(commit=False)
                profile = profileform.save(commit=False)
                address.user = user
                profile.user = user
                profile.save()
                address.save()
                login(request, user)
        else:
            signinform = SignInForm(data=request.POST)
            signupform = SignUpForm()

            if signinform.is_valid():
                login(request, signinform.get_user())
    else:
        signupform = SignUpForm()
        signinform = SignInForm()
        addressform = UserAddressForm()
        profileform = UserProfileForm()
    context = {'signupform': signupform,
               'signinform': signinform,
               'profileform':profileform,
               'addressform':addressform
               }
    return render(request, 'accounts/user_login.html', context)


def profileDetailView(request, id_):

    person = get_object_or_404(User, id=id_)
    profile = UserProfile.objects.get(user=person)
    print(person.userprofile)
    address = person.useraddress.all()

    return render(request, 'accounts/profileview.html', {'person': person, 'profile': profile, 'address': address})



def follow(request, id_):
    """
    follow a user or service
    :param request:
    :param id_:
    :return:
    """
    pass