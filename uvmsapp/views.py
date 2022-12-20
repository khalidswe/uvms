from email import message, message_from_binary_file
from pyexpat.errors import messages
import re
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from . models import *
from random import randint
from django.contrib.auth import logout

# Create your views here.

#index page
def IndexPage(request):
    return render(request,"app/index.html")

#home page
def Homepage(request):
    return render(request,"app/homepage.html")

#details page
def DetailsPage(request):
    return render(request,"app/details.html")

#signup page
def SignUpPage(request):
    return render(request,"app/signup.html")


# #login page
# def LogInPage(request):
#     return render(request,"app/login.html")


#Suggestion & complains page
def SugAndCompPage(request):
    return render(request,"app/sug&com.html")

#Rent page
def RentPage(request):
    return render(request,"app/rent.html")

#Book page
def BookPage(request):
    return render(request,"app/book.html")

#profile page
def Profile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user and user.role== "Student":
        stud = Student.objects.get(user_id=user)
        return render(request,"app/profile.html",{'user':user,'stud':stud})

#update profile page
def UpdateProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user and user.role== "Student":
        stud = Student.objects.get(user_id=user)
        return render(request,"app/updateprofile.html",{'user':user,'stud':stud})


#update profile
def UpdateProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)

    if user.role == "Student":
        stud = Student.objects.get(user_id=user)
        stud.name = request.POST['name']
        stud.student_id = request.POST['student_id']
        stud.address = request.POST['address']
        stud.department = request.POST['department']
        stud.contact = request.POST['contact']
        stud.pic = request.FILES['pic']
        stud.save()
        message = "Information Successfully Saved"
        return render(request,"app/profile.html",{'user':user,'stud':stud,'msg':message})


######### REGISTER_CODE ######

def SignUp(request):
    if request.POST['role']=="Student":
        role = request.POST['role']
        name = request.POST['name']
        email = request.POST['email']
        user_name =request.POST['user_name']
        password = request.POST['password']

        user = UserMaster.objects.filter(email=email) #here we can check email

        if user :
            message = "User already exist!!"
            return render(request,"app/index.html",{'msg':message})
        else:
            newuser = UserMaster.objects.create(role=role,email=email,user_name=user_name,password=password)
            newstudent= Student.objects.create(user_id=newuser,name=name)
            message = "Account Successfully Created."
            return render(request,"app/index.html",{'msg':message})
    
    elif request.POST['role']=="Officials":
        role = request.POST['role']
        name = request.POST['name']
        email = request.POST['email']
        user_name =request.POST['user_name']
        password = request.POST['password']

        user = UserMaster.objects.filter(email=email)

        if user :
            message = "User already exist!!"
            return render(request,"app/index.html",{'msg':message})
        else:
            newuser = UserMaster.objects.create(role=role,email=email,user_name=user_name,password=password)
            newofficials= Officials.objects.create(user_id=newuser,name=name)
            message = "Account Successfully Created."
            return render(request,"app/index.html",{'msg':message})
    else:
        message = "Please Select Your role!"
        return render(request,"app/signup.html",{'msg':message})


######### LOG IN CODE ######

def LogIn(request):
            if request.POST['role']=="Student":
                email = request.POST['email']
                password = request.POST['password']
 
                user = UserMaster.objects.get(email=email) 

                if user:
                    if user.password == password and user.role=="Student":
                        stu = Student.objects.get(user_id=user) 
                        request.session['id']=user.id
                        request.session['email']=user.email
                        request.session['role']=user.role
                        request.session['name']= stu.name

                        return redirect('homepage')
                
                    else:
                        message = "Password doesn't Match!!"
                        return render(request,"app/index.html",{'msg':message})
                else:
                    message = "User doesn't Exist!!"
                    return render(request,"app/index.html",{'msg':message})
            
            elif request.POST['role']=="Officials":
                email = request.POST['email']
                password = request.POST['password']
 
                user = UserMaster.objects.get(email=email) #just check email same or not

                if user:
                    if user.password == password and user.role=="Officials":
                        offi = Officials.objects.get(user_id=user)
                        request.session['id']=user.id 
                        request.session['email']=user.email
                        request.session['role']=user.role
                        request.session['name']=offi.name

                        return redirect('homepage')
                
                    else:
                        message = "Password doesn't Match!!"
                        return render(request,"app/index.html",{'msg':message})
                else:
                    message = "User doesn't Exist!!"
                    return render(request,"app/index.html",{'msg':message})
            else:
                message = "Select Role!!"   
                return render(request,"app/index.html",{'msg':message})

#search result 
def LogOut(request):
    user = request.session['id']
    userm = UserMaster.objects.get(id=user)
    logout(request)
    message = "Successfully Logged out."
    return render(request,"app/index.html",{'msg':message})

#search result 
def SearchResultPage(request):
    return render(request,"app/searchresult.html")

#search
def SearchBus(request):
    return render(request,"app/searchresult.html")