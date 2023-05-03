"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Journal.views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('', views.index, name="index"),
    # path('i18n/', include('django.conf.urls.i18n')),

    path('admin/', admin.site.urls),
    path('', include("Journal.urls")),
    path('account/', include('allauth.urls')),
    path('', include("WorkoutJournal.urls")),
    path('', include("Clubs.urls")),
    path('', include("account_register.urls")),
    path('', include("Presentation.urls")),
    path('', include("Notifications.urls")),

]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# htmx_urlpatterns = [
#
# ]

# urlpatterns += htmx_urlpatterns