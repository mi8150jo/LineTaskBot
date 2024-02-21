from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def top(request):
    """トップ画面"""
    return render(request,'account/login_page.html')