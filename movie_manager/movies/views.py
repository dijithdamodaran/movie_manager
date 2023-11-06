from django.shortcuts import render
from .models import movieinfo

# Create your views here.
def create(request):
    if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        desc=request.POST.get('summary')
        movie_obj=movieinfo(title=title,year=year,description=desc)
        movie_obj.save()
       
    return render(request,'create.html')

def list(request):
    movie_set=movieinfo.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set})

def edit(request):
    return render(request,'edit.html')