from django.shortcuts import render,redirect
from .models import Add
# Create your views here.
def index(request):
    adds = Add.objects.all()
    return render(request,'guestbook/index.html',{'adds': adds})

def add(request):
    new_Add= Add()
    new_Add.guest_name = request.POST['guest_name']
    new_Add.guest_say = request.POST['guest_say']
    new_Add.save()
    return redirect('/')

def delete(request,add_id):
    new_Add = Add.objects.get(id='add_id')
    new_Add.delete()
    return redirect('/')
