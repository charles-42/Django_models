from django.test import TestCase
from models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="charles", age=30, email="charles.beniac@gmail.com", mdp="secret")
        

    def test_for_test_method_name_length(self):
        """Animals that can speak are correctly identified"""
        charles = User.objects.get(name="charles")
        self.assertEqual(charles.for_test_method_name_length(), 7)


# Il faut ensuite lancer:

# ./manage.py test