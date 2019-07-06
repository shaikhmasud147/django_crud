from django.conf.urls import url
from employees import views
urlpatterns = [
    url(r'^add', views.add),
    url(r'^$', views.employee_view),
    url(r'^edit/(\d+)/$', views.employee_edit),
    url(r'^update/(?P<user_id>\d+)/$', views.employee_update),
    url(r'^delete/(\d+)/$', views.employee_delete),
]