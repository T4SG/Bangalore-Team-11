from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_mentor/$', views.new_mentor, name = 'new_mentor'),
    url(r'^mentor_debug/$', views.mentor_debug, name = 'mentor_debug'),
    url(r'^new_mentee/$', views.new_mentee, name = 'new_mentee'),
    url(r'^mentor_login/$', views.mentor_login, name = 'mentor_login'),
    url(r'^mentee_login/$', views.mentee_login, name = 'mentee_login'),
    #url(r'^mentor_page/(?P<mentor_id_in>\d+)/$', views.mentor_page, name = 'mentor_page'),
    url(r'^mentee_page/(?P<mentee_id_in>\d+)/$', views.mentee_login, name = 'mentee_page'),
]
