from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^movie-news/', views.movie_news),
]