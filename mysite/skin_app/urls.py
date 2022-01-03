from skin_app import views
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path(r'^submit/$',views.submit,name='submit'),
    path(r'^logout/$',views.logout, name='logout'),
]

