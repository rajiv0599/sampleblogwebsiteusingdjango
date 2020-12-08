from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def loginreg(request):
    

    if request.method == 'POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("Username already")
                messages.error(request," Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request," Email already taken")
                print('Email taken')
            elif not username.isalnum():
                messages.error(request," Username should only contain letters and numbers")
                print("Username should only contain letters and numbers")
                
                
                
            else:
                myuser=User.objects.create_user(username=username,email=email,password=password1,first_name=firstname,last_name=lastname)
                myuser.save()
                messages.success(request," Registered successfully")
                print('User created')
                
        else:
            print("password not matching")
            messages.error(request," Password not matching")
                
        return redirect("/login/form")
        


    else:
        return render(request,'loginregistration.html')


def login(request):
    if request.method=='POST':
        usernamee=request.POST['loginusername']
        passwordd=request.POST['loginpassword']
        myuser=auth.authenticate(username=usernamee,password=passwordd)
        if myuser is not None:
            auth.login(request,myuser)
            messages.success(request,' Login successful')
            return redirect('/')
        else:
            messages.error(request," Invalid credentials")
            return redirect('/login/form')
    else:
        return render(request,'loginregistration.html')

    

def logout(request):
    auth.logout(request)
    messages.success(request,' You have been logged out.')
    return redirect('/')