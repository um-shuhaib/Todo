from django.shortcuts import render,redirect
from django.views import View
from TodoApp.forms import UserRegisterForm,UserLoginForm,TodoForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class UserRegisterView(View):
    def get(self,request):
        form=UserRegisterForm()
        return render(request,"register.html",{"form":form})
    def post(self,request):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            # form.save()  will not encript the pass so
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"registration successful")
            return redirect("login")
        else:
            messages.warning(request,"not registered")
            return redirect("register")
        


class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request):
        username=request.POST.get("username")
        passw=request.POST.get("password")
        res = authenticate(request,username=username,password=passw)
        if res:
            messages.success(request,"Login successful")
            return redirect("home")
        else:
            messages.warning(request,"Invalid Credential")
            return redirect("login")
        
class HomeView(View):
    def get(self,request):
        return render(request,"home.html")
    

class CreateTodoView(View):
    def get(self,request):
        form=TodoForm()
        return render(request,"createTodo.html",{"form":form})
