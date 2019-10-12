from django.shortcuts import render,redirect
from testapp.models import BasicInfo,Opprtunity
from testapp.forms import BasicInfoForm,OpprtunityForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
def home_view(request):
    return render(request,'testapp/home.html')


def sign_view(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['username']
        first_name=request.POST['f_name']
        last_name=request.POST['l_name']
        password=request.POST['pwd']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('sign')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Id Taken')
            return redirect('sign')
        else:
            user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
            user.save()
            return redirect('login')
    else:
        return render(request,'testapp/register.html')
def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('career')
        else:
            messages.info(request,'Invalid credential')
            return redirect('login')
    else:
        return render(request,'testapp/login.html')
def logout_view(request):
    auth.logout(request)
    return redirect('/')
def career_view(request):
    opp=Opprtunity.objects.all()
    return render(request,'testapp/career.html',{'opp':opp})

def apply_view(request):
    form=BasicInfoForm()
    if request.method=='POST':
        form=BasicInfoForm(request.POST)
        if form.is_valid:
            form.save()
            
            return submit_view(request)
    return render(request,'testapp/apply.html',{'form':form})
def submit_view(request):
    return render(request,'testapp/submit.html')
