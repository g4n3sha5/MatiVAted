from django.urls import path
from . import views

urlpatterns = [
    path('bjjournal/', views.BJJournalIndex, name="BJJournalIndex"),
    path('dashboard/', views.dashboard, name='dashboard')

]
htmx_urlpatterns = [

]
urlpatterns += htmx_urlpatterns
