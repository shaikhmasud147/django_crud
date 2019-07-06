from django.conf.urls import url
from testapp1 import views

urlpatterns = [
    url(r'^temp/', views.template_views),
]