from django.conf.urls import url
from testapp2 import views

urlpatterns = [
    url(r'^morning/', views.good_morning_message),
    url(r'^afternoon/', views.good_Afternoon_message),
    url(r'^evening/', views.good_evening_message),
    url(r'^night/', views.good_night_message),
]