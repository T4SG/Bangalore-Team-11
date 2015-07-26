from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_mentor/$', views.new_mentor, name = 'new_mentor'),
    url(r'^mentor_debug/$', views.mentor_debug, name = 'mentor_debug'),
    url(r'^new_mentee/$', views.new_mentee, name = 'new_mentee'),
    url(r'^mentor_login/$', views.mentor_login, name = 'mentor_login'),
    url(r'^mentee_login/$', views.mentee_login, name = 'mentee_login'),
]
