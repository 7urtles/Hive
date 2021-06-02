from detection.views import SettingsView
from django.test import TestCase
from detection.models import Company, Movement
from django.utils import timezone
from datetime import datetime
from django.urls import reverse
from django.urls import resolve

# Create your tests here.
class Create_Company_Test(TestCase):
    def test_setUp(self):
        Company.objects.create(company="CompanyTest_1", entered=5, exited=4, current=1, capacity=15),
        Company.objects.create(company="CompanyTest_2", entered=10, exited=8, current=2, capacity=24)
        self.assertEqual(Company.objects.count(), 2)

class Create_Movement_Test(TestCase):
    def test_setUp(self):
        Movement.objects.create(company="CompanyTest_1", timeIn=datetime.now(tz=timezone.utc), timeOut=datetime.now(tz=timezone.utc))
        Movement.objects.create(company="CompanyTest_2", timeIn=datetime.now(tz=timezone.utc), timeOut=datetime.now(tz=timezone.utc))
        self.assertEqual(Movement.objects.count(), 2)

class Create_URL_Tests(TestCase):
    def test_home_url(self):
        response = resolve('/')
        self.assertEqual(response.func, SettingsView.as_view())