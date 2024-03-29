from django.shortcuts import render
from django.views import View

from channels.layers import get_channel_layer

# Create your views here.


class Test(View):
    def get(self, request):
        return render(request, 'chat/test.html')


class Main(View):
    def get(self, request):
        return render(request, 'chat/main.html')
    
    
class Login(View):
    def get(self, request):
        return render(request, 'chat/login.html')
    
    
class Logout(View):
    def get(self, request):
        pass
    
    
class Home(View):
    def get(self, request):
        return render(request, 'chat/home.html')
    
class Chatting(View):
    def get(self, request):
        return render(request, 'chat/chatting.html')
    
class Register(View):
    def get(self, request):
        return render(request, 'chat/register.html')