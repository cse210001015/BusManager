from django.urls import path
from . import views
urlpatterns=[
    path('',views.getRoutes,name='routes'),
    path('admin-bus-view/', views.adminBusesViews.as_view(), name='Admin Buses API'),
    path('admin-bus-view/<pk>/', views.adminBusViews.as_view(), name='Admin Bus API'),
    path('admin-location-view/', views.adminLocationsViews.as_view(), name = 'Admin Locations API'),
    path('admin-location-view/<pk>/', views.adminLocationViews.as_view(), name = 'Admin Location API'),
    path('admin-routes-view/', views.adminRoutesViews.as_view(), name = 'Admin Routes API'),
    path('admin-routes-view/<pk>/', views.adminRouteView.as_view(), name = 'Admin Route API')
]
