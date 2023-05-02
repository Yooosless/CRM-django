from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import Signup,AddRecordForm
from .models import Record
# Create your views here.
def home(request):
    records= Record.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"login successful")
            return redirect('home')
        else:
            messages.success(request, "login failed")
            return redirect('home')
        
    return render(request,'home.html',{'records':records})



def logoutUser(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')

def registerUser(request):
    form=Signup(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"Successfully Registered")
            return redirect('home')
    else:
        form=Signup()
        return render(request,'register.html',{'form':form})
    return render(request, 'register.html', {'form':form})



def record(request,pk):
    if request.user.is_authenticated:
        record=Record.objects.get(id=pk)
        return render(request, 'record.html', {'record':record})
    else:
        messages.success(request, "You must be LOGGED IN to view this")
        return redirect('home')
    

def delete_ID(request,pk):
    if request.user.is_authenticated:
        deleteID=Record.objects.get(id=pk)
        deleteID.delete()
        messages.success(request, "Record deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be LOGGED IN to DELETE this")
        return redirect('home')
    
def addRecord(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				addRecord=form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')



def update_record(request, pk):
	if request.user.is_authenticated:
		record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')