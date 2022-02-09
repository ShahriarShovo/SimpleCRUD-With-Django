import imp
from os import name
from django.urls import path
from crud import views

app_name="crud"

urlpatterns = [
    path('',views.index,name='index'),
    path('addEmployee/',views.addEmployee,name='addEmployee'),
    path('edit/<int:id>/',views.edit,name='addEmployee'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
