from django.urls import path
from . import views 

urlpatterns = [
	path('', views.index, name='index'),
	path('update/', views.stock_update),
	path('api/', views.topStocks),
	path('api/signup', views.email_signup),
]
