# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.tasks import change_balance

def index(request):
	if request.GET.get('username') != '' and request.GET.get('username') != None:
		username = request.GET.get('username')
		try: 
			value = float(request.GET.get('balance'))
		except ValueError:
			return redirect('/')
		change_balance.delay(username, value)
	if request.GET.get('username') == None:
		return render(request, "main/index.html")
	return redirect('/')

# Create your views here.
