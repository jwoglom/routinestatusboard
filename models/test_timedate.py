from unittest import TestCase
from .timedate import *

class TestTime(TestCase):
    def test_midnight(self):
        self.assertEqual(Time.of('12:00am'), Time(0, 0))
        self.assertEqual(Time.of('12am'), Time(0, 0))
        self.assertEqual(Time.of('00:00'), Time(0, 0))
        self.assertEqual(Time.of(0), Time(0, 0))

    def test_noon(self):
        self.assertEqual(Time.of('12:00pm'), Time(12, 0))
        self.assertEqual(Time.of('12pm'), Time(12, 0))
        self.assertEqual(Time.of('12:00'), Time(12, 0))
        self.assertEqual(Time.of(1200), Time(12, 0))

    def test_9am(self):
        self.assertEqual(Time.of('9:00am'), Time(9, 0))
        self.assertEqual(Time.of('9am'), Time(9, 0))
        self.assertEqual(Time.of('09:00am'), Time(9, 0))
        self.assertEqual(Time.of('09am'), Time(9, 0))
        self.assertEqual(Time.of('09:00'), Time(9, 0))
        self.assertEqual(Time.of(900), Time(9, 0))

    def test_930am(self):
        self.assertEqual(Time.of('9:30am'), Time(9, 30))
        self.assertEqual(Time.of('09:30'), Time(9, 30))
        self.assertEqual(Time.of(930), Time(9, 30))

    def test_9pm(self):
        self.assertEqual(Time.of('9:00pm'), Time(21, 0))
        self.assertEqual(Time.of('9pm'), Time(21, 0))
        self.assertEqual(Time.of('09:00pm'), Time(21, 0))
        self.assertEqual(Time.of('09pm'), Time(21, 0))
        self.assertEqual(Time.of('21:00'), Time(21, 0))
        self.assertEqual(Time.of(2100), Time(21, 0))

    def test_930pm(self):
        self.assertEqual(Time.of('9:30pm'), Time(21, 30))
        self.assertEqual(Time.of('21:30'), Time(21, 30))
        self.assertEqual(Time.of(2130), Time(21, 30))

class TestDuration(TestCase):
    def test_mins(self):
        self.assertEqual(Duration.of('0m'), Duration(0, 0))
        self.assertEqual(Duration.of('10m'), Duration(0, 10))
        self.assertEqual(Duration.of('50m'), Duration(0, 50))
        self.assertEqual(Duration.of('60m'), Duration(1, 0))
        self.assertEqual(Duration.of('70m'), Duration(1, 10))

    def test_hours(self):
        self.assertEqual(Duration.of('0h'), Duration(0, 0))
        self.assertEqual(Duration.of('1h'), Duration(1, 0))
        self.assertEqual(Duration.of('2h'), Duration(2, 0))

    def test_both(self):
        self.assertEqual(Duration.of('0h0m'), Duration(0, 0))
        self.assertEqual(Duration.of('0h60m'), Duration(1, 0))
        self.assertEqual(Duration.of('0h70m'), Duration(1, 10))
        self.assertEqual(Duration.of('1h60m'), Duration(2, 0))
        self.assertEqual(Duration.of('1h70m'), Duration(2, 10))
