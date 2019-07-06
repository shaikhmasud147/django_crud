from django.conf.urls import url
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'users/signin.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', user_views.signup, name='signup'),
]