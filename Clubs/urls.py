from django.urls import path
from . import views, views_schedule
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('clubs/', views.ClubsIndex, name="clubsIndex"),
    path('leaveClub', views.leaveClub, name="leaveClub")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

htmx_urlpatterns = [
    path('clubs/members', views.clubMembers, name="clubMembers"),
    path('clubs/removemember/<int:id>', views.memberRemove, name="memberRemove"),
    path('clubs/trainings', views.clubTrainings, name="clubTrainings"),
    path('clubs/schedule', views_schedule.clubSchedule, name="clubSchedule"),
    path('clubs/schedule/delete/<str:type>/<str:day>/<str:hour>/<int:clubID>',
         views_schedule.removeTrainingSchedule, name="removeTrainingSchedule"),
    path('clubs/schedule/add/<str:type>/<str:day>', views_schedule.addTrainingModal, name="addTrainingModal"),
    # path('clubs/schedule/add/<str:type>/<str:day>', views_schedule.scheduleAddTraining, name="scheduleAddTraining"),
    path('clubs/list', views.clubsList, name="clubsList"),
    path('clubs/<int:id>', views.singleClubView, name="singleClubView"),
    path('clubs/request/<int:requestID>', views.handleRequest, name="handleRequest"),
    path('clubs/<int:clubID>/member/<int:userID>/', views.memberProfile, name="memberProfile")
    # path('clubs/join/<int:id>', views.joinClub, name="joinClub")


]


urlpatterns += htmx_urlpatterns