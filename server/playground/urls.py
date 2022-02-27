from django.urls import path
from . import views

#django looks for urlpatterns object
urlpatterns = [
    path('hello/', views.say_hello)
]