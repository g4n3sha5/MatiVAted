from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.urladjuster, name='urladjuster'),
    path('create/', views.create, name='create'),
]
