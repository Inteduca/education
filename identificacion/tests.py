from django.test import TestCase
from django.contrib.auth.models import User

class GetEmailTest(TestCase):
    d=User()
    d.email="email.email@email"
    d.save()
    def getemail(self, d):
        e=d.email
        print(e)





# Create your tests here.
