from django.shortcuts import render

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

    return render(request , 'receipes.html') 
