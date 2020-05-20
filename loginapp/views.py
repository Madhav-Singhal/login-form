from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
# def basic(request):
#     return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        val3 = request.POST['username']
        val4 = request.POST['password']

        user = auth.authenticate(username=val3, password=val4)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return redirect('loginapp:login')

    else:
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        val1 = request.POST['first_name']
        val2 = request.POST['last_name']
        val3 = request.POST['username']
        val4 = request.POST['password']
        val5 = request.POST['confirm']

        if val4 == val5:
            if User.objects.filter(username=val3).exists():
                
                
                return render(request, 'register.html')
            else:


                user = User.objects.create_user(username = val3, password = val4, first_name = val1, last_name = val2)
                user.save()
                return redirect("loginapp:login")

        else:
            return redirect('loginapp:register')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
            
            
    
        




    


