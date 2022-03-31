from django.shortcuts import render,redirect
from .models import Dorm
from django.contrib.auth.models import User,auth
from django.contrib import messages

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

def loginForm(request):
    return render(request, 'login.html')

def addUser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    
    if password == repassword :
        if User.objects.filter(username = username).exists():
            messages.info(request, "This username already been used")
            return redirect('/createForm')
        elif User.objects.filter(email = email).exists():
            messages.info(request, "This email already been used")
            return redirect('/createForm')
        else : 
            user = User.objects.create_user(
            username = username,
            password = password,
            email = email,
            first_name = firstname,
            last_name = lastname
            )
            user.save()
            return redirect('/')
    else :
        messages.info(request, "Password dosen't match")
        return redirect('/createForm')
    
    

def tableView(request):
    return render(request, 'table.html')

def queryDB(request):
    #Query data from model
    data = Dorm.objects.all()
    return render(request, 'table.html' , {'dorms' : data}) 

def loginPage(request):
    return render(request, 'login.html')

'''
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
    '''
    
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    #เช็คว่าชื่อกับรหัสตรงกับที่บันทึกไว้หรือป่าว
    user = auth.authenticate(username = username , password = password)
    
    if user is not None : 
        auth.login(request, user)
        return redirect('/')
    else :
        messages.info(request, "Username or Password are invalid")
        return redirect('/loginForm')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def postCard(request):
    return render(request, 'postCard.html')