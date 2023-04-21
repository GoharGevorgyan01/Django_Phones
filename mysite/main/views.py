from django.shortcuts import render
from .models import Phones # viewsy cucadrakan faylerna en inchy petqa cuyc ta grum enq stex
# Create your views here.
def home(request):
    phone=Phones.objects.all()
    return render(request,'home.html',context={
        'phone':phone
    })
#phon popoxakani mej enq iran pahum vor html um et anunov dimenq