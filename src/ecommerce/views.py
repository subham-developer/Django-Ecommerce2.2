from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from .forms import Contact_form,LoginForm

def home_page(request):
    context = {
        'title':'Home Page',
        'content':'Welcome! to Home Page'
    }
    if request.user.authenticate():
        context['premium_content':'Yeahhhh']
    return render(request,'home_page.html',context)


def about_page(request):
    context = {
        'title':'About Page',
        'content':'Welcome! to About Page'
    }
    return render(request,'home_page.html',context)


def contact_page(request):
    contact_form = Contact_form(request.POST or None)
    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('fullname'))
    context = {
        'title':'Contact Page',
        'content':'Welcome! to Contact Page',
        'contact_form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,'contact/view.html',context)


def login_view(request):
    loginForm = LoginForm(request.POST or None)
    if request.method == 'POST':
        print(request.POST)
    context = {
        'title':'Login Page',
        'content':'Welcome! to Login Page',
        'login_Form': loginForm
    }
    if loginForm.is_valid():
        print(loginForm.cleaned_data)
        print(request.POST)
        username = loginForm.cleaned_data.get("LoginId")
        password = loginForm.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            # context['login_form'] = LoginForm()
            return redirect("/")
        else:
            print('Error')
    return render(request,'Auth/login.html',context)