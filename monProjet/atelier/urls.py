from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.consulter, name='consulter'),
    path('notes/back/', views.retourner, name='retourner'),
]