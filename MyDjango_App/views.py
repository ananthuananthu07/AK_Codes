from django.shortcuts import render, redirect
from django.http import HttpResponse
from MyDjango_App.models import AccessRecord, UserProfileInfo
from . import forms
from .forms import UserForm, UserProfileForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# def index(request):
#     webpage_data = AccessRecord.objects.order_by('date')
#     dict_content = {
#         'access_records': webpage_data,
#     }
#     return render(request, 'firstapp/index.html', context=dict_content)
#


def index(request):
    dict_content = {
        'text': "Hello World", 'number': "100"}
    return render(request, 'firstapp/index.html', context=dict_content)


def form_view(request):
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('validation success')
            print(f'name: {form.cleaned_data["name"]}')
            print(f'email: {form.cleaned_data["email"]}')
            print(f'description: {form.cleaned_data["desc"]}')

            # Process the form data here
            return redirect('index')  # Redirect to a success page after processing the form
    else:
        form = forms.FormName()
    return render(request, 'firstapp/form.html', context= {'form': form})


def web_page_view(request):
    form = forms.WebPage1()

    if request.method == "POST":
        form = forms.WebPage1(request.POST)

        if form.is_valid():
            form.save(commit=True)

    return render(request, "firstapp/form.html", context={"form": form})


def other(request):
    return render(request, "firstapp/other.html")


def relative(request):
    return render(request, "firstapp/relative_url.html")


def registration(request):
    return render(request, "firstapp/registration.html")


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data= request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, "firstapp/registration.html", context={
        "user_form": user_form, "profile_form": profile_form, "registered" : registered
    })


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Your account is inactive")

        else:
            print("Login Failed")
            return HttpResponse("Invalid Login details")
    else:
        return render(request, "firstapp/login.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

