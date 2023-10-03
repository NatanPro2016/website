from django.shortcuts import render
from .models import Studet, Sector

# Create your views here.



def register(request):
    sectors = Sector.objects.all()
    if request.method == "POST":
        first_name =  request.POST['first_name']
        middle_name =  request.POST['middle_name']
        last_name =  request.POST['last_name']
        email =  request.POST['email']
        sex = request.POST['sex']
        phone_number =  request.POST['phone_number']
        sector = request.POST['sector']
        sector = Sector.objects.get(id=sector)
        type = request.POST['type']

        
      


        if first_name == '' or  middle_name =='' or last_name == '' or email == '':
            return render(request, 'register.html', {'sectors': sectors, 'message': 'please make sure to fill all forms'})

        else:
            new_data = Studet(first_name = first_name, middle_name = middle_name, last_name = last_name, email = email, sex = sex, phone_number=phone_number, type= type, sector = sector , status='PE')
            new_data.save()
            
            return render( request, 'success.html' , {'message':'you are sucessfully registerd we are make sure that we delver a mail through given email '})
        

    return render(request, 'register.html', {'sectors': sectors })

def report(request):
    return render(request, 'report.html')