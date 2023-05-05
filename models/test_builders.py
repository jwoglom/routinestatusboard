from unittest import TestCase
from .routine import *
from .builders import *

class TestBuildRoutine(TestCase):
    def test_builder(self):
        self.assertEqual(
            routine(name='Lunch', start='12:15pm', duration='45m'),
            Routine(name='Lunch', start=Time(12, 15), end=Time(13, 0))
        )
        self.assertEqual(
            routine(name='Lunch', start='12:45pm', duration='1h45m'),
            Routine(name='Lunch', start=Time(12, 45), end=Time(14, 30))
        )
