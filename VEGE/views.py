from django.shortcuts import render ,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        print('Receipe name:', receipe_name)
        print('Receipe description:', receipe_description)
        print('Receipe image:', receipe_image)
       
        Receipe.objects.create(receipe_image = receipe_image ,
                                receipe_name = receipe_name,
                                receipe_description = receipe_description)
        return redirect('/receipes/')
       
    queryset= Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))



    context ={'receipes': queryset}
    return render(request , 'receipes.html', context) 

def update_receipe(request ,id):
    queryset = Receipe.objects.get(id = id)
  
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        
        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes/')

    context ={'receipes': queryset}
    return render(request,'update_receipe.html', context)

        
def delete_receipe(request ,id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')

def login_page(request):
    return render(request, 'login.html')


def register_page(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('Username')
        password=request.POST.get('password')



        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username)
        user.set_password(password)
        user.save()

        return redirect('/register/')



    return render(request, 'register.html')

   
   
 

