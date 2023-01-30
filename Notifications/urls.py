from django.urls import path
from . import views


urlpatterns = [


]
htmx_urlpatterns = [
    path('notifications', views.notifications, name="notifications"),

]
urlpatterns += htmx_urlpatterns
#   path('view/', views.listView, name = "listView")