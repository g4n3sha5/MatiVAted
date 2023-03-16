from django.test import TestCase, Client
from django.urls import resolve, reverse
from WorkoutJournal.views import BJJournalIndex, yourSessions
from WorkoutJournal.models import TrainingSession, Technique, Suggestion
import json
from django.contrib.auth.models import User
class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.yourSessions_url = reverse('yourSessions')
        self.addSession_url = reverse('addSession')
        self.BJRIndex_url = reverse('bjjournal')
        self.user = User.objects.create_user('john', 'lehnon@com.pl', 'password')
        self.client.login(email='lehnon@com.pl', password = 'password')

    def test_yourSessions_GET(self):
        response = self.client.get(self.yourSessions_url)
        self.assertEquals(response.status_code, 200)
    def test_addSession_GET(self):
        response = self.client.get(self.addSession_url)
        self.assertEquals(response.status_code, 200)

    # def test_addSession_POST(self):
    #     TrainingSession.objects.create(hoursLength = 2, type= "GI" )
    #     response = self.client.post(self.addSession_url,{
    #         'hoursLength' : 2,
    #         'type' : 'GI'
    #     })
    #     self.assertEquals(response.status_code, 302)
    #
    def test_index_GET(self):
        response = self.client.get(self.BJRIndex_url)
        self.assertEquals(response.status_code, 200)
