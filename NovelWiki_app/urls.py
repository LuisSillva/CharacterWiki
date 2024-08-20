from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_character, name='create_character'),
    path('create/shadow_slave/<int:character_id>/', views.create_shadow_slave, name='create_shadow_slave'),
    path('create/lotm/<int:character_id>/', views.create_lotm, name='create_lotm')
]
