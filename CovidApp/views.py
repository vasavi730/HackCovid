from django.shortcuts import render

# Create your views here.


def food(request):
	return render(request,'food.html')

def rice(request):
	return render(request,'rice.html')

def cart(request):
	return render(request,'cart.html')

def labrequest(request):
	return render(request,'labrequest.html')