from django.shortcuts import render
from pass_app.forms import UserForm, UserProfileInfoForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def special(requests):
    return HttpResponse('You are logged in , Nice!')


@login_required
def user_logout(requests):
    logout(requests)
    return HttpResponseRedirect(reverse('index'))


def register(requests):

    registered = False

    if requests.method == 'POST':
        user_form = UserForm(data=requests.POST)
        profile_form = UserProfileInfoForm(data=requests.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in requests.FILES:
                profile.profile_pic = requests.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(requests, 'pass_app/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print('Someone tried to login and failed!')
            print(f'Username: {username} and password {password}')
            return HttpResponse('invalid login details')

    else:
        return render(request, 'pass_app/login.html', {})
