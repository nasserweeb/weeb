from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
from . import models
from .form_compny import compny_form
from .models import compny2

def form_creat(request):
    return render(request,'iput_form.html',{})

def backend1(request):

       #v1 = request.POST['txtname']
       #v2 = request.POST['txtemail']
       #v3 = request.POST['txtage']
       #v4 = request.POST['txtbarty']
       new=models.compny2(fullname=request.POST['txtname'],email=request.POST['txtemail'],age=request.POST['txtage'],barty=request.POST['txtbarty'])
    #   new.fullname=v1
     #  new.email =v2
      # new.age =v3
       #new.barty =v4
       new.save()
       return HttpResponseRedirect('/hpt1')
      
def form_updat(request,id):
    data= models.compny2.objects.get(id=id)# use get with data
   # data=models.compny2.objects.filter(age__gte=31) #use filter with data[]
    print('the type is : '+str(data))
    return render(request,'updat_form.html',{'id_form':id,'data':data})
def backend2(request,id):
    new = models.compny2(id=id,fullname=request.POST['txtname'], email=request.POST['txtemail'], age=int(request.POST['txtage']),barty=request.POST['txtbarty'])
    new.save()
    return HttpResponseRedirect('/hpt1')
def backend3(request,id):
    old= models .compny2 (id=id)
    old.delete()

    return HttpResponseRedirect('/hpt1')

def index(request):
     data=models.compny2.objects.all()
     return render (request,'form_show.html',{'d':data})

def reg(request):
     form= compny_form(request.POST or None )
     obj=compny2()
     if form.is_valid():
        if not form.cleaned_data['bart']:
             obj.barty="1995-1-1"
        else:
             obj.barty=form.cleaned_data['bart']

        obj.fullname=form.cleaned_data["name"]
        obj.email = form.cleaned_data['email']
        obj.age=form.cleaned_data['age']
        obj.save()
        return HttpResponseRedirect('/hpt1')
 
     
     return render (request,'forms_test.html',{'f':form})

 





