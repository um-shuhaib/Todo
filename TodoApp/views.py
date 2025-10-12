from django.shortcuts import render,redirect
from django.views import View
from TodoApp.forms import UserRegisterForm,UserLoginForm,TodoForm,TodoEditForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from TodoApp.models import Todo
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy

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
            login(request,res)
            messages.success(request,"Login successful")
            return redirect("home")
        else:
            messages.warning(request,"Invalid Credential")
            return redirect("login")
        
# class HomeView(View):
#     def get(self,request):
#         if request.user.is_authenticated:
#             todo=Todo.objects.filter(user=request.user,status="pending")
#             return render(request,"home.html",{"todo":todo})
#         else:
#             messages.success(request,"You must Login first")
#             return render(request,"home.html",{"msg":"No Data"})

# class HomeView(TemplateView):
#     template_name="home.html"
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context["todo"]=Todo.objects.filter(user=self.request.user).exclude(status="completed")
#         return context


class HomeView(ListView):
    model=Todo
    context_object_name="todo"
    template_name="home.html"

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).exclude(status="completed")


    

# class CreateTodoView(View):
#     def get(self,request):
#         form=TodoForm()
#         return render(request,"createTodo.html",{"form":form})
    
#     def post(self,request):
#         form_instances=TodoForm(request.POST)
#         print(request.user)
#         if form_instances.is_valid():
#             Todo.objects.create(**form_instances.cleaned_data,user=request.user)
#             messages.success(request,"Todo Added")
#             return redirect("home")
            
class CreateTodoView(CreateView):
    template_name="createTodo.html"
    form_class=TodoForm
    model=Todo
    # success_url=reverse_lazy("home")

    def form_valid(self, form):
        Todo.objects.create(**form.cleaned_data,user=self.request.user)
        messages.success(self.request,"Todo Added")
        return redirect("home")
    
    def form_invalid(self, form):
        messages.success(self.request,"invalid input")
        return super().form_invalid(form)
        





# class DeleteView(View):
#     def get(self,request,**kwargs):
#         todo=Todo.objects.get(id=kwargs.get("id"))
#         todo.delete()
#         messages.warning(request,"Todo deleted succesfully")
#         return redirect("home")


class DeleteView1(DeleteView):
    model=Todo
    pk_url_kwarg='id'
    success_url=reverse_lazy("home")
    template_name="confirm_delete.html"




    
# class UpdateView(View):
#     def get(self,request,**kwargs):
#         todo=Todo.objects.get(id=kwargs.get("id"))
#         form=TodoEditForm(instance=todo)
#         return render(request,"todoUpdate.html",{"form":form})
    
#     def post(self,request,**kwargs):
#         todo=Todo.objects.get(id=kwargs.get("id"))
#         form_instances=TodoEditForm(request.POST,instance=todo)
#         if form_instances.is_valid():
#             form_instances.save()
#             messages.warning(request,"Todo deleted succesfully")
#             return redirect("home")

class UpdateView1(UpdateView):
    model=Todo
    form_class=TodoEditForm
    template_name="todoUpdate.html"
    pk_url_kwarg="id"
    success_url=reverse_lazy("home")










class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Logout succesfully")
        return redirect("login")
