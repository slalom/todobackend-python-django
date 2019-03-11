from django.urls import path, include
from .views import ListTodosView
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', ListTodosView.as_view(), name="todos-all")
]
