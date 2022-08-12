from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('bloodgroups',views.bloodgroups,name='bloodgroups'),
    path('search',views.search,name='search'),
    path('donar',views.donar,name='donar'),
    path('bloodtips',views.bloodtips,name='bloodtips'),
    path('bloodfacts',views.bloodfacts,name='bloodfacts'),
    path('accounts/register/',views.register,name="register"),
    path('accounts/login/',views.login,name="login"),
    path('accounts/register/',views.logout,name="logout"),
    path('services',views.services,name='services'),
    path('donarhome',views.donarhome,name='donarhome'),
    path('patienthome',views.patienthome,name='patienthome'),
    path('pservices',views.pservices,name='pservices'),
    path('pregistration',views.pregistration,name='pregistration'),
    path('dsearch',views.dsearch,name='dsearch'),
]