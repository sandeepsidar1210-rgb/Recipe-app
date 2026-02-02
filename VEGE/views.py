from django.shortcuts import render ,redirect
from .models import *

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
        return redirect('receipes')
       
    queryset= Receipe.objects.all()
    context ={'receipes': queryset}
    return render(request , 'receipes.html') 
   
 

