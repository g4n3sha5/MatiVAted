from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('about/<str:section>/', views.aboutSection, name = "aboutSection")

]
htmx_urlpatterns = [




]


urlpatterns += htmx_urlpatterns