from django.urls import path
from . import views


urlpatterns = [
    # path('notifications/', views.notifications, name="notifications"),
    # path('allNotifications/', views.allNotifications, name="allNotifications"),
    path('clearNotifications/', views.clearNotifications, name="clearNotifications"),

]
htmx_urlpatterns = [


]
urlpatterns += htmx_urlpatterns
#   path('view/', views.listView, name = "listView")