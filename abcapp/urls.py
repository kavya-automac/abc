
from django.urls import path
from . views import *


urlpatterns = [
    path('',ABCApi.as_view()),
    path('demo_db/', DemoView.as_view(), name='demo-view'),

]
