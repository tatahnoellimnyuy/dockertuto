from django.urls import path
from . import views,models



app_name='core'

urlpatterns = [
	path('',views.IndexView,name='index'),
	]