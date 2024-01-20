from django.urls import path
from . import views
urlpatterns=[
    path('',views.getRoutes,name='routes'),
    path('admin-bus-view/', views.adminBusesViews.as_view(), name='Admin Buses API'),
    path('admin-bus-view/<pk>/', views.adminBusViews.as_view(), name='Admin Bus API'),
    path('admin-location-view/', views.adminLocationsViews.as_view(), name = 'Admin Locations API'),
    path('admin-location-view/<pk>/', views.adminLocationViews.as_view(), name = 'Admin Location API')
]
