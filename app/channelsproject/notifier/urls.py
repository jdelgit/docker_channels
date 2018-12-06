from django.urls import path
from .views import HomeView, someform

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('myform', someform, name='myform')
]