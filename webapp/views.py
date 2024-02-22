from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from allauth.socialaccount.models import SocialAccount
from taskmanagement.models import Task
import logging

def home(request):
    # ログインしているとき
    if request.user.is_authenticated:
        social_accounts = SocialAccount.objects.filter(user=request.user)
        tasks = Task.objects.filter(user_ID=request.user)
        logging.debug(tasks)

        return render(request, "remindbot/home.html", {
            "social_accounts": social_accounts,
            "tasks": tasks,
        })