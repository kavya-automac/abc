
from django.urls import path
from . import views


urlpatterns = [
    path('',views.DemoApi.as_view()),

]
