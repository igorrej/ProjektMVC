from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ksiazek, name='lista_ksiazek'),
    path('dodaj/', views.dodaj_ksiazke, name='dodaj_ksiazke'),
    path('edytuj/<int:pk>/', views.edytuj_ksiazke, name='edytuj_ksiazke'),

    path('usun/<int:pk>/', views.usun_ksiazke, name='usun_ksiazke'),

]
