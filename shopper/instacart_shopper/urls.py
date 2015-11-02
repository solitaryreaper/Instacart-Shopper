from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^funnel.json/$', views.funnel_analytics, name='funnel_analytics'),
    url(r'^background_check/$', views.background_check, name='background_check'),
    url(r'^confirmation/$', views.application_confirmation, name='confirmation'),
    url(r'^update/$', views.update_application, name='update'),    
    url(r'^edit/$', views.edit_application, name='edit')         
]