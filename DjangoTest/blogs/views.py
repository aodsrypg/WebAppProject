from django.shortcuts import render
from .models import Dorm
from django.contrib.auth.models import User

# Create your views here.
def hello(request):
    tags = ['ชาย','หญิง','หอนอก','หอใน','ราคาต่ำกว่า 6000']
    rating = 3
    return render(request,'index.html',
                  {'name':'Finding roommate',
                   'author':'Suriyaporn Amornsinsawat',
                   'tags':tags, 
                   'rating':rating
                   })
    
def findRoomPage(request):
    return render(request, 'findRoomPage.html')

def createForm(request):
    return render(request, 'form.html')

def addBlogs(request):
    name = request.POST['Name']
    description = request.POST['Description']
    return render(request, 'result.html',{'Name':name,'Description':description})

def tableView(request):
    return render(request, 'table.html')

def queryDB(request):
    #Query data from model
    data = Dorm.objects.all()
    return render(request, 'table.html' , {'dorms' : data}) 

def loginPage(request):
    return render(request, 'login.html')

def addLogin(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    
    User.object.create_user(
        username = username,
        password = password,
        email = email,
        first_name = firstname,
        last_name = lastname
    )
    user.save()
    return render(request, 'result.html')