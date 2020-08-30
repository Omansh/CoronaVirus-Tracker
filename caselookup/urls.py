from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='caselookup-home'),
    path('countrywisecases/', views.CountrywiseStats, name='caselookup-countrywisecase'),
    path('statewisecases/', views.statewisecases, name='caselookup-statewisecases'),
    path('casestimeline/', views.casestimeline, name='caselookup-casestimeline'),
]
