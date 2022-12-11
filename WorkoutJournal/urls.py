from django.urls import path
from . import views

urlpatterns = [
    path('bjjournal/', views.BJJournalIndex, name="BJJournalIndex")


]
htmx_urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addSession/', views.addSession, name="addSession"),
    path('techniques/', views.techniques, name="techniques"),
    path('addTechnique/', views.techniques, name="addTechnique")
]


urlpatterns += htmx_urlpatterns
