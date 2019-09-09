from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^send_email$', views.send_login_email, name='send_logi_email'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
]

