from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('view/<str:pk>', views.viewPlayer, name="view_player"),
    path('delete/<str:pk>', views.deletePlayer, name="delete_player")
]
