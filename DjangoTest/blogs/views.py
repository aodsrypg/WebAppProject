from django.shortcuts import render,redirect
from blogs.models import Dorm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,InvalidPage
#from insertrecord.models import insertemprecord

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
    # sex = request.POST['sex']
    # phone = request.POST['phone']
    # line_ID = request.POST['line_ID']
    # habit = request.POST['habit']
    
    print(request.POST)
    
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
            last_name = lastname,
            # sex = sex,
            # phone = phone,
            # line_ID = line_ID,
            # habit = habit
            )
            user.save()
            messages.info(request, "Sign up Successfully")
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
        messages.info(request, "Login Successfully")
        return redirect('/')
    else :
        messages.info(request, "Username or Password are invalid")
        return redirect('/loginForm')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def postCard(request):
    posts=None
    # users=None
    posts=Dorm.objects.all()
    # users=User.objects.all()

    paginator=Paginator(posts,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        postperPage=paginator.page(page)
    except (EmptyPage,InvalidPage):
        postperPage=paginator.page(paginator.num_pages)


    return render(request, 'postCard.html',{'posts':postperPage})


def postIng(request,Dorm_dormName):
    
    try:
        name = Dorm.objects.get(dormName=Dorm_dormName)
    except Exception as e :
        raise e
    return render(request, 'postDetail.html',{'dormName':name})
    
    # information=None
    # information=Dorm.objects.get(dormName=Dorm_dormName)

    # return render(request,'postDetail.html',{'information':information})
    
def resultdetaIl(request) :
    try:
        print('owliang')
        print(id)
        id = Dorm.objects.get(id=id)
        
    except Exception as e :
        raise e
    return render(request, 'result.html',{'id':id})
    
    
    
    
    
    
def addPost(request):
    
    # users=User.objects.all()
   
    #ISOwner = 'haveRoom' in request.POST.keys()
    username = request.POST['Username']
    sex = request.POST['sex']
    dormName = request.POST['dormName']
    mateNumber = request.POST['mateNumber']
    rent = request.POST['rent']
    location = request.POST['location']
    dormDescription = request.POST['dormDescription']
    mateHabit = request.POST['mateHabit']
    comment =request.POST['comment']
    separateBed = request.POST['separateBed']
    utilityBillType = request.POST['utilityBillType']
    contact = request.POST['contact']
    rentShare = request.POST['rentShare']
    
    if 'haveRoom' in request.POST:
        haveRoom = request.POST['haveRoom']
    else:
        haveRoom = "ยังไม่มีห้อง"
        
    #haveRoom = request.POST['haveRoom']
    
    # print('Owliang')
    # print(dormName)
    #print(request.POST)

    #ISOwner = 'haveRoom' in request.POST.keys()
    
    # print(ISOwner)
   
    dorm = Dorm(
    Username=username,
    sex = sex,
    dormName = dormName,
    mateNumber = mateNumber,
    rent = rent,
    location = location,
    dormDescription = dormDescription,
    mateHabit = mateHabit,
    comment = comment,
    separateBed = separateBed,
    utilityBillType = utilityBillType,
    rentShare = rentShare,
    contact = contact,
    haveRoom = haveRoom
    )
    dorm.save()
    messages.info(request, "แบบฟอร์มได้รับการบันทึกแล้ว")
    #return render(request, 'postCard.html')
    
    return redirect('/postCard')
    
    # return render(request, 'result.html',{'dormName':dormName, 'mateNumber':mateNumber, 'rent':rent, 'location':location, 'dormDescription':dormDescription,
    #                                       'mateHabit':mateHabit, 'comment':comment, 'separate':separateBed, 'bill':utilityBillType, 'rentShare':rentShare, 'haveRoom':haveRoom})

def search(request):
    posts = Dorm.objects.filter(location__contains=request.GET['title'])
    posts = Dorm.objects.filter(dormName__contains=request.GET['title'])
    
    return render(request,'postCard.html',{'posts':posts})

def result(request): #  ?id=2
    posts=Dorm.objects.all()
    dorm = None
    for post in posts:
        if post.id == int(request.GET['id']):
            dorm = post
            break
    # print(request.GET['id'])
    return render(request,'result.html',{'id':request.GET['id'], 'dorms' : dorm})