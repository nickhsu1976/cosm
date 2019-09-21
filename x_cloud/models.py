from django.db import models

# Create your models here.

class Customer(models.Model):
	customer_id = models.CharField(max_length=10)
	customer_name = models.CharField(max_length=20)
	password = models.CharField(max_length=16, null=False, default="")
	tax_id = models.CharField(max_length=8)
	tel = models.CharField(max_length=12)
	fax = models.CharField(max_length=12)
	address = models.CharField(max_length=100)
	designer = models.ForeignKey('Designer', blank=True, null=True, related_name='Customer_Designer', on_delete=models.SET_NULL)

	def __str__(self):
		return self.customer_name


GENDER_CHOICE = (
	    ('男性', '男性'),
	    ('女性', '女性'),
	)

class Designer(models.Model):
	designer_id = models.CharField(max_length=10)
	designer_name = models.CharField(max_length=10)
	gender = models.CharField(max_length=4, choices=GENDER_CHOICE, default='女性')
	phone = models.CharField(max_length=12)
	address = models.CharField(max_length=100)

	def __str__(self):
		return self.designer_name


class Member(models.Model):
	member_id = models.CharField(max_length=10)
	member_name = models.CharField(max_length=10)
	gender = models.CharField(max_length=4, choices=GENDER_CHOICE, default='女性')
	phone = models.CharField(max_length=12)
	tel_for_home = models.CharField(max_length=12)
	career = models.CharField(max_length=30)
	address = models.CharField(max_length=100)
	email = models.EmailField()
	line_id = models.CharField(max_length=60)
	designer = models.ForeignKey('Designer', blank=True, null=True, related_name='Member_Designer', on_delete=models.SET_NULL)

	def __str__(self):
		return self.member_name