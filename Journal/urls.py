from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.listManager, name='listManager'),
    path('create/', views.create, name='create'),

]
htmx_urlpatterns = [
    path('removeList/<int:id>', views.removeList, name="removeList"),
    path('removeItem/<int:listId>/<int:itemId>', views.removeItem, name="removeItem"),
    path('create_menu/', views.create, name='create_menu')
]
urlpatterns += htmx_urlpatterns
#   path('view/', views.listView, name = "listView")