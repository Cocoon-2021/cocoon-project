from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from preg_form.models import *


def index(request):
    return render(request,'index.html')
    # return HttpResponse("Hello, world. You're at the preg_form index.")


def reg_tb_entry(request):
    if request.method=='POST':
        vfname=request.POST['fname']
        vlname=request.POST['lname']
        vdptm=request.POST['dptm']
        vusername=request.POST['username']
        vstream=request.POST['stream']
        vpassword=request.POST['psw']
        vemail=request.POST['email']
        vmob_no=request.POST['mobile']
        print(vfname,vlname)
        insert_tb=reg_tb(fname=vfname,lname=vlname,dptm=vdptm,username=vusername,
        stream=vstream,password=vpassword,email=vemail,mob_no=vmob_no)
        insert_tb.save()
        return render(request,'login.html',{'out':"Successfully Registered"})
    else:
        return render(request,'index.html',{'fail':"Successfully Failed"})


def login(request):
    if request.method == 'POST':
        vemail=request.POST['email']
        vpassword=request.POST['psw']
        check=reg_tb.objects.all().filter(email=vemail,password=vpassword)
        if check:
            for x in check:
                request.session['id']=x.id
                myid=request.session['id']
                show=reg_tb.objects.all().filter(id=myid)
                print(show)
                return render(request,'profile.html', {'display':show})
            else:
                return render(request,'login.html')
        else:
            return render(request,'login.html')









