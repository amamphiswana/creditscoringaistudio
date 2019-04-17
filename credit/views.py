from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext, loader
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context
from django.template import *
from .models import Post
import psycopg2
import json


def home(request):
	conn = psycopg2.connect(dbname="creditscoring", user="postgres", password="cr3dit", host="35.196.21.144", port=5432)
	cur = conn.cursor()

	cur.execute('''
		  SELECT * FROM client_results''')

	rows = cur.fetchall()
	datas=[]
	for i in range(len(rows[0])):
		datas.append(rows[0][i])
	client_info=datas

	context={"client_info":client_info}
	if request.method == "POST":
		if request.POST.get("ID") and request.POST.get("Gender") and request.POST.get("Age") and request.POST.get("Salary") and request.POST.get("Loan_amount") and request.POST.get("Term"):
			post = Post()
			post.ID = request.POST.get("ID")
			post.Gender = request.POST.get("Gender")
			post.Age = request.POST.get("Age")
			post.Salary = request.POST.get("Salary")
			post.Loan_amount = request.POST.get("Loan_amount")
			post.Term = request.POST.get("Term")
			post.save()

			return render(request,'index.html',context)
		else:
			return render(request,'index.html',context)


	return render(request,'index.html',context)
#
def createpost(request):
	return render(request,'Page2.html')
