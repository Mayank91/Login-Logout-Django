from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.contrib import auth
from django.core.context_processors import csrf
from forms import ArticleForm

# view starts from here

def home(request):
    name = "Mayank"
    html = "hello %s its working mann!!!" %name
    return HttpResponse(html)

class HelloTemplate(TemplateView):
    template_name = "index.html"
    def get_context_data(self,**kwargs):
        context = super(HelloTemplate,self).get_context_data(**kwargs)
        context['name'] = "Mayank "
        return context

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)
@csrf_exempt
def auth_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username = username ,password = password)
    if user is not None :
        auth.login(request,user)
        return HttpResponseRedirect('/loggedin/')
    else:
        return HttpResponseRedirect('/invalid_login/')

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def loggedin(request):
    return render_to_response('loggedin.html',{"full_name" : request.user.username})

def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    return render_to_response('registration.html',args)

def success(request):
    return HttpResponseRedirect('/login/')

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('index.html')
    else:
        form = ArticleForm(request.POST)
        con = {}
        con.update(csrf(request))
        con['form'] = form
        return render_to_response("form.html",con)
