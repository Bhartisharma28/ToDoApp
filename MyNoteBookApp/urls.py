from django.urls import path
from . import views
urlpatterns=[
path('', views.Home, name='Home'),
path('update/<str:pk>/', views.update, name='update'),
path('delete/<str:pk>/', views.delete, name='delete'),
]
