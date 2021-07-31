from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Visit
# Create your views here.

def home(request):
    visits = Visit.objects.all()
    return render(request,"home.html",{'visits':visits})

def detail(request,id):
    visit = get_object_or_404(Visit, pk = id)
    return render(request,'detail.html',{'visit':visit})

def new(request):
    return render(request,'new.html')

def create(request) :
    new_visit = Visit()
    new_visit.name = request.POST['name']
    new_visit.body = request.POST['body']
    new_visit.date =  timezone.now()
    new_visit.save()
    return redirect('home')

def edit(request, id) :
    edit_visit = Visit.objects.get(id=id)
    return render(request, 'edit.html',{'visit':edit_visit})

def update(request,id):
    update_visit = Visit.objects.get(id = id)
    update_visit.name = request.POST['name']
    update_visit.body = request.POST['body']
    update_visit.date =  timezone.now()
    update_visit.save()
    return redirect('detail',update_visit.id)

def delete(request,id):
    delete_visit = Visit.objects.get(id=id)
    delete_visit.delete()
    return redirect('home')

def hobby(request):
    return render(request,'hobby.html')
    
def favorite(request):
    return render(request,'favorite.html')

def exhibit(request):
    return render(request,'exhibit.html')