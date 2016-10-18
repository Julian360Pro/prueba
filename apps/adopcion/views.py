from django.shortcuts import render
from django.http import HttpResponse


def index_adopcion(request):
	return HttpResponse("Esta es la pagina principal de la app adopcion")

# Create your views here.
