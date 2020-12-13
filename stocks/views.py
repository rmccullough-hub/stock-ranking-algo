from django.shortcuts import render
from .models import Stock, Member

from django.http import JsonResponse
from django.http import HttpResponse
from django.core.mail import send_mail

from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StockSerializer, MemberSerializer
from .webscraping import stock_data, ranking
from .tickers import stocks as stock_tickers
from time import sleep

index = never_cache(TemplateView.as_view(template_name="index.html"))

def stock_update(request):

	Stock.objects.all().delete()

	top_stocks = []

	for ticker in stock_tickers[:7]:
		try:
			sleep(60)
			top_stocks.append(stock_data(ticker))
		except Exception as e:
			print(e)
			print(ticker)


	top_stocks.sort(key=ranking, reverse=True)

	for stock in top_stocks[:6]:
		ticker = stock['ticker']
		print(stock['score'])
		new_stock = Stock(
			eps=float(stock['eps']), 
			leverage_ratio=float(stock['leverage_ratio']), 
			roce=float(stock['roce']), 
			score=stock['score'],
			pe=stock['pe'],
			name=stock['name'],
			image_url=stock['image_url'],
			income_statement = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}',
			balance_sheet = f'https://finance.yahoo.com/quote/{ticker}/balance-sheet?p={ticker}',
			cash_flow = f'https://finance.yahoo.com/quote/{ticker}/cash-flow?p={ticker}',
			ticker = stock['ticker'],
			)

		new_stock.save()
	
	stock_objects = Stock.objects.all()
	stock_message = ''

	for stock in stock_objects:
		stock_message += str(stock.name) + ' ' + str(stock.ticker) + ',\n'

	send_mail(
		"This Week's Best Stocks",
		stock_message,
		'ryanmcculloughuc@gmail.com',
		[member.email for member in Member.objects.all()],
		fail_silently=True,
		)

	return HttpResponse('Working')

@api_view(['GET'])
def topStocks(request):

	stocks = list(Stock.objects.all())

	serializer = StockSerializer(stocks, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def email_signup(request):

	serializer = MemberSerializer(data=request.data)
	if serializer.is_valid():
		member = Member(first_name=request.data['first_name'], email=request.data['email'])
		if len(Member.objects.filter(email=member.email)) == 0:
			member.save()

			send_mail(
			    'Confirmation',
			    'You are now on our email list.',
			    'ryanmcculloughuc@gmail.com',
			    [member.email],
			    fail_silently=True,
			)
			print(member.email)
	return Response(serializer.data)