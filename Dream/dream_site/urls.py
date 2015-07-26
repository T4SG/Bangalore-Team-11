from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_mentor/$', views.new_mentor, name = 'new_mentor')
]
