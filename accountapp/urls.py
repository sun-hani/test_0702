from django.urls import path
from accountapp.views import hello_friends

appname = 'accountapp'

urlpatterns = [
    path('hello_friends/', hello_friends, name='hello!'),
]
