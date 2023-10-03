from django.shortcuts import render
from system.models import News, SectorMessage, Feedback


def index(request):
    sectors = SectorMessage.objects.all()
    
    if request.method == "POST":
        full_name =  request.POST['full_name']
        email =  request.POST['email']
        message =  request.POST['message']
    

        
      


        if full_name == '' or  email =='' or message == '':
            return render(request, 'index.html', {'sectors': sectors, 'message': 'please make sure to fill all forms'})

        else:
            new_data = Feedback(email = email, full_name = full_name, message = message)
            new_data.save()
            return render(request, 'success.html' )
        
   
    return render(request, 'index.html', {'sectors': sectors})


def news(request):
    news = News.objects.all()
    return render(request, 'news.html' ,{'news':news}) 






    