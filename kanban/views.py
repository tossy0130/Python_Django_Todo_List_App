from django.shortcuts import render, redirect

# サインアップ用　ビュー
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse
# Create your views here.

def index(request):
   # return HttpResponse("トップページ仮")
   return render(request, "kanban/index.html")

def home(request):
    return render(request, "kanban/home.html")


def signup(request):
    # ============ サインアップ用
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("kanban:home")
    
    else:
        # Djangoに標準で搭載されているフォームクラス => UserCreationForm()
        form = UserCreationForm()
        
    context = {
        "form" : form
    }
    
    return render(request, 'kanban/signup.html', context)