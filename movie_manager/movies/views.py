from django.shortcuts import render

# Create your views here.
def create(request):
    if request.POST:
        print(request.POST.get('title'))
        print(request.POST.get('year'))
       
    return render(request,'create.html')

def list(request):
    movie_data={
        'movies' :[
            {
                'title':'godfather',
                'year':1900,
                'summary': 'story of underworld king',
                'sucess':False,
                'img':'godfather.jpg'
            },
            {
                'title': 'titanic',
                'year': 2002,
                'summary': '',
                'sucess': True,
                'img':'titanic.jpg'
            },
            {
                'title': 'avatar',
                'year': 1990,
                'summary': 'story of underworld king',
                'sucess': False,
                'img':'avatar.jpg'
            }
        ]
    }
    
    return render(request,'list.html',movie_data)

def edit(request):
    return render(request,'edit.html')