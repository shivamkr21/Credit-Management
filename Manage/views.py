from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import emp, trnf
from django.contrib.auth.models import User

ids=0

def index(request):
 	return render(request,'Manage/index.html',{})

@csrf_exempt
def detail(request):
    global ids
    if(request.POST):
        print(request.POST)
        ids=request.POST.get('id')
        print ids
    return HttpResponse('success')

def details(request):
    cont={}
    uss=emp.objects.all()
    for i in uss:
        if(int(ids)==i.id):
            cont={'name':i.name,'email':i.email,'age':i.age,'gen':i.gender,'credit':i.credit,'phn':i.phone}
            print i.name, i.email
    print cont
    return render(request,'Manage/detail.html',cont)


def member(request):
    cont={}
    contt={}
    us=emp.objects.all()
    for i in us:
        cont={i.id:{'id':i.id,'name':i.name,'email':i.email}}
        contt.update(cont)
    return render(request,'Manage/member.html',contt)

def transferfrom(request):
    cont={}
    contt={}
    us=emp.objects.all()
    for i in us:
        cont={i.id:{'name':i.name,'crd':i.credit}}
        contt.update(cont)
    return render(request,'Manage/transfer.html',contt)

def transferto(request):
    cont={}
    contt={}
    us=emp.objects.all()
    for i in us:
        cont={i.id:{'name':i.name,'crd':i.credit}}
        contt.update(cont)
    return render(request,'Manage/transfer2.html',contt)

@csrf_exempt
def trncrd(request):
    if(request.POST):
        print(request.POST)
        cd=0
        cdd=0
        n1=""
        n2=""
        credt=request.POST.get('crdt')
        print credt
        idm=request.POST.get('id')
        us=emp.objects.all()
        uss=emp.objects.all()
        for i in us:
            if(i.id==int(ids)):
                cd=i.credit
                n1=i.name
        for i in uss:
            if(i.id==int(idm)):
                cdd=i.credit
                n2=i.name
        cd=cd-int(credt)
        cdd=cdd+int(credt)
        emp.objects.filter(id=ids).update(credit=cd)
        emp.objects.filter(id=idm).update(credit=cdd)
        print n1 , n2
        input1=trnf.objects.create(cfrom=n1,cto=n2,credit=int(credt))

    return HttpResponse('success')

def transaction(request):
    us=trnf.objects.all()
    datas={"data":us}
    return render(request,'Manage/transaction.html',datas)
