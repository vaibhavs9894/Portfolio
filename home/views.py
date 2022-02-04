from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    skill_list = Skill.objects.all()
    project_list = Project.objects.all()
    ctx = {
        'skill_list': skill_list,
        'project_list': project_list,
        'title': 'Home', 
        'hactive':'class=active',     
    }
    return render(request, 'home.html',context=ctx)

def about(request):
    ctx = {
         'aactive':'class=active',  
    }
    return render(request, 'about.html',context=ctx)

def contact(request):
    form = ContactForm()                        # blank form creation
    if request.method == "POST":                # agar form bhar diya
        form = ContactForm(request.POST)        # form create kro but user k input k sath
        if form.is_valid():                     # agar sab badiya
            form.save()                         # save the information to database
            messages.success(request, "Thank you for your message.")
            return redirect('/contact')         # reload the page or goto some page
    ctx ={
        'form': form,
        'cactive':'class=active', 
    }
          
   
    return render(request, 'contact.html',context=ctx)