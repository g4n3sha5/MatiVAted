from django.urls import path
from . import views

urlpatterns = [
    path('bjjournal/', views.BJJournalIndex, name="bjjournal")


]
htmx_urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addSession/', views.addSession, name="addSession"),

    path('editSession/<int:id>/<int:orderIndex>', views.editSession, name="editSession"),
    path('yourSessions/', views.yourSessions, name="yourSessions"),
    path('techniques/', views.techniques, name="techniques"),
    path('technique/<int:id>/', views.singleTechniqueView, name="singleTechniqueView"),
    path('session/<int:id>/<int:orderIndex>/', views.singleSessionView, name="singleSessionView"),
    path('session/<int:id>/edit', views.editSession, name="editSession"),
    path('session/<int:id>/remove', views.removeSession, name="removeSession"),


]


urlpatterns += htmx_urlpatterns