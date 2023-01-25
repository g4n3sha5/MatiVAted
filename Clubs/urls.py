from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('clubs/', views.ClubsIndex, name="clubsIndex")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

htmx_urlpatterns = [
    path('clubs/members', views.clubMembers, name="clubMembers"),
    path('clubs/trainings', views.clubsTrainings, name="clubsTrainings"),
    path('clubs/schedule', views.clubsSchedule, name="clubsSchedule"),
    path('clubs/list', views.clubsList, name="clubsList"),
    path('clubs/<int:id>', views.singleClubView, name="singleClubView"),
    # path('clubs/join/<int:id>', views.joinClub, name="joinClub")


]


urlpatterns += htmx_urlpatterns