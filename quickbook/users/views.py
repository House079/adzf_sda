from ast import literal_eval

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import User, CATEGORIS


# Create your views here.

def user(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.website = form.cleaned_data.get("website")
            user.profile.position = form.cleaned_data.get("position")
            user.save()
            messages.success(request, "User successfully added.")
            return HttpResponseRedirect(request.path)

    else:
        form = UserRegisterForm()
    return render(request, 'users/user.html', {"form": form})

"""Jak otwierasz pierwszy raz wyswietla pusta forme i form wysyla do html"""

def remove_user(request):
    """"""
    list_of_users = User.objects.all()
    seperator = ";$"
    user_id = ""
    first_name = ""
    last_name = ""
    website = ""
    postion = ""
    date = ""
    for user in list_of_users:
        user_id += str(user.pk) + seperator
        first_name += str(user.first_name) + seperator
        last_name += str(user.last_name) + seperator
        website += str(user.profile.website) + seperator
        postion += dict(CATEGORIS)[str(user.profile.position)] + seperator
        date += str(user.date_joined) + seperator
    context = {
        "user_id": user_id[0:-2],
        "first_name": first_name[0:-2],
        "last_name": last_name[0:-2],
        "website": website[0:-2],
        "position": postion[0:-2],
        "date": date[0:-2]
    }

    return render(request, 'users/remove_user.html', context)

def remove_users_be(request):
    print("I got into reqiest")
    if request.user.is_superuser and request.method == "POST":
        user_list_to_delete = literal_eval(request.POST.dict()["removal_user_list"])
        for user_pk in user_list_to_delete:
            user_to_delete = User.objects.get(pk=user_pk)
            user_to_delete.delete()
        HttpResponse('200')
    HttpResponse('403')
