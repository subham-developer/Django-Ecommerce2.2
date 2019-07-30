from django.http import HttpResponse
from django.shortcuts import render
from .forms import Contact_form

def home_page(request):
    context = {
        'title':'Home Page',
        'content':'Welcome! to Home Page'
    }
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