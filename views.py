from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	params={'name':'shashi','place':'Laxmi Nagar','gender':'Male'}
	return render(request,'index.html',params)

def about(request):
	return HttpResponse('''<h1> Details </h1><a href ="http://www.youtube.com">About Us</a>''')

def space_remove(request):
	return HttpResponse("space remover <a href = '/'>back</a>")

def removepunc(request):
	print(request.GET.get('text','default'))
	return HttpResponse("removepunc")