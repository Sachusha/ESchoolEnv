from django.conf.urls import url
from django.urls import path

from .views import *
from .import views

app_name = 'static_settings'

urlpatterns = [
    url(r'^$', index, name='IndexForms'),
    url(r'static_settings', schoolprofile, name='schoolprofile'),
    url(r'school_delete/(?P<pk>\d+)/$', school_delete, name='school_delete'),
    url(r'school_edit/(?P<pk>\d+)/$', school_edit, name='school_edit'),
    url(r'school_view/<int:pk>/', views.SchoolProfileView.as_view(), name='school_view'),
    # url(r'school_update/<int:pk>/', views.SchoolProfileupdate.as_view(), name='school_update'),
    # url(r'school_delete/<int:pk>/', views.SchoolProfileDelete.as_view(), name='school_delete'),
]
