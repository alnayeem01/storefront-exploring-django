from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# a view is a request handler which sends response according to hte request.

def hello_world(hello):
	return HttpResponse('Hello world!')