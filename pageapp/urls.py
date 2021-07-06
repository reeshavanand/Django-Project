from django.urls import path
from . import views

urlpatterns = [
      path('play', views.play, name='play'),
      path('add', views.add, name='add'),

      path('', views.index, name='home'),
      
      path('contact', views.contact, name='contact'),
      path('cart', views.cart, name='cart'),
      path('about', views.about, name='about')
      ]