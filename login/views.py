from django.shortcuts import render
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
# Create your views here.
def login(request):
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/dashboard')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def invalid(request):
    return render_to_response('invalid.html')
    
