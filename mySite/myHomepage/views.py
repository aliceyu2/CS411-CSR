from django.shortcuts import render
from django.http import HttpResponse
import pymysql
pymysql.install_as_MySQLdb()
def goToHomepage(request):
	return render(request, 'homepage2.html')