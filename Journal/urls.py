from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.urladjuster, name='urladjuster'),
    path('create/', views.create, name='create'),
    path('remove/<int:id>', views.removeList, name="remove")

]
#   path('view/', views.listView, name = "listView")