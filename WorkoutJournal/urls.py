from django.urls import path
from . import views

urlpatterns = [
    path('bjjournal/', views.BJJournalIndex, name="bjjournal")


]
htmx_urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addSession/', views.addSession, name="addSession"),
    path('yourSessions/', views.yourSessions, name="yourSessions"),
    path('techniques/', views.techniques, name="techniques"),
    path('technique/<int:id>/', views.singleTechniqueView, name="singleTechniqueView"),
    path('session/<int:id>/', views.singleSessionView, name="singleSessionView"),
    path('session/<int:id>/edit', views.editSession, name="editSession"),


]


urlpatterns += htmx_urlpatterns