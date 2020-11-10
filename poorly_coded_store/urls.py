from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buying', views.buying),
    path('checkout', views.checkout),
    path('reset', views.reset),

]
