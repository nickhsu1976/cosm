from django.forms import ModelForm, TextInput, Select
from django import forms
from .models import *


class CustomerForm(forms.Form):
	username = forms.CharField(label="帳號", max_length=20)
	password = forms.CharField(label="密碼", max_length=20)