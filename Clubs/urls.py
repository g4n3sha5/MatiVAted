from django.urls import path
from . import views

urlpatterns = [
    path('clubs/', views.ClubsIndex, name="clubs")


]
htmx_urlpatterns = [



]


urlpatterns += htmx_urlpatterns