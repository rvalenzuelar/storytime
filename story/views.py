# from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Line

def home(request):
	# return HttpResponse("HOLA MI ARDILLA HERMOSA!!!")
	# return render_to_response('story/home.html',{'hello': "A otro perro con ese hueso"})
	return render_to_response('story/home.html', {'lines': Line.objects.all()})

