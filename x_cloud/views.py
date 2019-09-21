from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sessions.models import Session
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from x_cloud.models import *
from .forms import *

# Create your views here.

def Login(request):
	if request.method == 'POST':
		login_form = CustomerForm(request.POST)
		if login_form.is_valid():
			customer_id = request.POST['customer_id'].strip()
			login_password = request.POST['password']
			try:
				user = Customer.objects.get(customer_id=customer_id)
				if user.password == login_password:
					request.session['customer_id'] = user.customer_id
					request.session['customer_name'] = user.customer_name
					messages.add_message(request, messages.SUCCESS, '您已成功登入了!')
					return redirect('x_cloud:index')
				else:
					messages.add_message(request, messages.WARNING, '密碼錯誤! 請再檢查一次!')
			except:
				messages.add_message(request, messages.WARNING, '找不到使用者!')
		else:
			messages.add_message(request, messages.INFO, '請檢查輸入的欄位內容!')
	else:
		login_form = CustomerForm()

	return render(request, 'Login.html', locals())

def Index(request):
	if 'customer_id' in request.session:
		customer_id = request.session['customer_id']
		customer_name = request.session['customer_name']

	return render(request, 'index.html', locals())