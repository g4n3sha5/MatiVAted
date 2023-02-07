from django.urls import path
from . import views


urlpatterns = [
    path('notifications/', views.notifications, name="notifications"),

]
htmx_urlpatterns = [


]
urlpatterns += htmx_urlpatterns
#   path('view/', views.listView, name = "listView")