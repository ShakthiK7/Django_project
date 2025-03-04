from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('register/')
            else:
                user_reg= User.objects.create_user(username=username, email=email, password=password)
                user_reg.save()
                messages.info(request, "Successfully Created")
                return redirect('/')
        else:
            messages.info(request, "Password Doesn't Match")
            return redirect('register/')

    return render(request,'reg.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Login Success")
            return redirect('/')
        else:
            messages.info(request, "Login Invalid")
            return redirect('register/')
        
    return render(request, 'log.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
