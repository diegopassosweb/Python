
from django.urls import path
from mysite_project import views

urlpatterns = [
    path('',views.home, name='home'),
    path('usuarios/', views.usuarios,name='listagem_usuarios')
]
