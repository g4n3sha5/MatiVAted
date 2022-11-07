from django.urls import path, include
from .views import acc_register
urlpatterns = [
    path('register/', acc_register),
    path('account/', include('allauth.urls'))
]