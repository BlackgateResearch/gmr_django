from django.test import TestCase
from models import Track

class SimpleTest(TestCase):
    
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        Track.objects.all()
