#coding:utf-8
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from books.models import Book
from django.shortcuts import render_to_response
from django.template import Template,Context,RequestContext

# Create your views here.
def display_search_form(request):
    return render(request,'search.html') 

def search(request):
    books = Book.objects.filter(title__icontains=request.GET['q']) 
    return render_to_response('search_results.html',{'books':books}) 

def first_page(request):
    return HttpResponse('welcome to django!!')

def template_page(request):
    s = 'welcome to template'
    html = '''<p>{{template}}</p>'''
    t  = Template(html)
    c = Context({'template':s})
    m = t.render(c)
    return HttpResponse(m) 

def success(request):
    return render_to_response('success.html',{})

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject')
        if not request.POST.get('message',''):
            errors.append('Enter a message')
        if request.POST.get('email') and ('@' not in request.POST.get('email')):
            errors.append('Enter a valid emailaddress')
        if not errors:
            return HttpResponseRedirect('success/')#当前页面的URL + "success/"
    return render_to_response('contact_form.html',{'subject':request.POST.get('subject',''),'message':request.POST.get('message',''),'email':request.POST.get('email',''),'errors':errors})
