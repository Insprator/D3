from django.shortcuts import render


# Create your views here.
def index(request):
    a = 'Nikita'
    return render(request, 'index.html', context= {'name': a})