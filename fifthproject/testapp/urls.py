from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^datetimeview/', views.date_time_view),
]