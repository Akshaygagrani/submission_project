from  django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name = 'welcome'),
    path('detail/', views.details, name= 'details'),  # linkin detail keword to detail view
    path('deep_info/<int:pk>/', views.deep, name = 'deep_info_student'),
    path('add_info/', views.add, name='add_student'),
]
