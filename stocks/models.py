from django.db import models

class Stock(models.Model):
	eps = models.FloatField()
	roce = models.FloatField()
	leverage_ratio = models.FloatField()
	score = models.FloatField(default=0)
	ticker = models.CharField(max_length=200)
	name = models.CharField(max_length=200, default='Stock')
	pe = models.FloatField(max_length=200, default=0)
	image_url = models.URLField(max_length=200, null=True)
	balance_sheet = models.URLField(max_length=200, null=True)
	income_statement = models.URLField(max_length=200, null=True)
	cash_flow = models.URLField(max_length=200, null=True)

class Member(models.Model):
	first_name = models.CharField(max_length=200)
	email = models.EmailField(max_length=254)