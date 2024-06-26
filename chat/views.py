from django.shortcuts import render, redirect
from django.views import View
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth import authenticate, login, logout
from .models import UsersTbl
from django.db import IntegrityError 
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Create your views here.


class Test(View):
    def get(self, request):
        return render(request, 'chat/test.html')


class Main(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        
        return render(request, 'chat/main.html')
    
    
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        
        return render(request, 'chat/login.html')
    
    def post(self, request):
        received_data = request.POST.dict()
     
        username = received_data.get("username")
        password = received_data.get("password")
        
        # Basic validation
        errors = {}
        if not username:
            errors['username'] = 'Username is required.'
        if not UsersTbl.objects.filter(username=username).exists():
            errors['username'] = 'Username does not exists.'
        if not password:
            errors['password'] = 'Password is required.'

        if not errors:
            user = authenticate(request=request, username=username, password=password)
            if user:
                print("User login successfully.")
                login(request=request, user=user)
                return redirect("home")
            else:
                errors['Login Failed'] = 'Incorrect Password !!'
        
        # Create or update the context dictionary
        context = {'errors': errors}
        return render(request, 'chat/login.html', context=context)
    
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("main")
    
class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            
            # Sending user list 
            all_users = UsersTbl.objects.all()
            context = {"current_user":request.user, "all_users":all_users}

            return render(request, 'chat/home.html', context=context)
        
        return redirect("main")
    
class Chatting(View):
    def get(self, request, id):
        # chatting with the person You want 
        chat_person = UsersTbl.objects.get(id=id)
        current_user = request.user
        
        context = {"current_user":current_user, "chat_person":chat_person}
        return render(request, 'chat/chatting.html', context=context)
    
class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        
        return render(request, 'chat/register.html')
    
    def post(self, request):
        received_data = request.POST.dict()
        
        first_name = received_data.get("first_name")
        last_name = received_data.get("last_name")
        username = received_data.get("username")
        email = received_data.get("email")
        password = received_data.get("password")
        
        # Basic validation
        errors = {}
        if not first_name:
            errors['first_name'] = 'First name is required.'
        if not last_name:
            errors['last_name'] = 'Last name is required.'
        if not username:
            errors['username'] = 'Username is required.'
        elif UsersTbl.objects.filter(username=username).exists():
            errors['username'] = 'Username already exists.'
        if not email:
            errors['email'] = 'Email is required.'
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors['email'] = 'Invalid email format.'
        if not password:
            errors['password'] = 'Password is required.'

        # If there are no validation errors, proceed with creating the user
        if not errors:
            # Check if the username already exists
            if UsersTbl.objects.filter(username=username).exists():
                print("Error: Username already exists.")
            else:
                print("First Name:", first_name)
                print("Last Name:", last_name)
                print("Username:", username)
                print("Email:", email)
                
                # Create a new user instance and save it to the database
                try:
                    new_user = UsersTbl(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password
                    )
                    new_user.save()
                    
                    user = authenticate(request=request, username=username, password=password)
                    if user:
                        print("User created successfully.")
                        login(request=request, user=user)
                        return redirect("home")
                    else:
                        print("Fail !!")
                except Exception as e:
                    errors['Adding new user']='DB Error is : '+str(e)
         
        # Create or update the context dictionary
        context = {'errors': errors}
        return render(request, 'chat/register.html', context=context)
        
        
        