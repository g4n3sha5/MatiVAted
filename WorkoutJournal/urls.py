from django.urls import path
from . import views

urlpatterns = [
    path('bjjournal/', views.BJJournalIndex, name="BJJournalIndex")


]
htmx_urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addSession/', views.addSession, name="addSession"),
    path('techniques/', views.techniques, name="techniques"),
    path('technique/<int:id>/', views.singleTechniqueView, name="singleTechniqueView"),
]


urlpatterns += htmx_urlpatterns
