from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.test, name='test'),
    url(r'^dash/', views.dashboard, name='dashboard'),
    url(r'^dash2/', views.dash2, name='dash2'),
]