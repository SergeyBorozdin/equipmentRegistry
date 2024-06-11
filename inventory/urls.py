from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('equipment_list/', views.equipment_list, name='equipment_list'),
    path('add_equipment/', views.add_equipment, name='add_equipment'),
    path('delete_equipment/', views.delete_equipment, name='delete_equipment'),
]