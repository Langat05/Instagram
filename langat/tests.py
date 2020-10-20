from django.test import TestCase
from django.contrib.auth.models import User
from .models Image, Profile, Comment


# Create your tests here.


class ProfileTescase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('langat')
        cls.profile = Profile(profile_pic='', bio ='Brought up in Kenya',cls.user = user)

    def test_instance(cls):
        cls.assertTrue(isinstance(cls.profile, Profile))        

    def save_method_test(self):
        self.profile.save_profile()
