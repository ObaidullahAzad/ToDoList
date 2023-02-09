from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="list"),
	path('Edit/<str:num>/', views.updateTask, name="Edit"),
	path('delete/<str:num>/', views.deleteTask, name="delete"),
]