import unittest
from classes.bar import *
from classes.guests import *
from classes.songs import *
from classes.room import *

class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest(15, "beyonce", False)
        self.guest2 = Guest(20, "beyonce", False)
        self.guest3 = Guest(10, "britney", False)
    
    def test_guest_has_money(self):
        self.assertEquals (15, self.guest1.money)

    def test_guest_has_fave_song(self):
        self.assertEquals ("beyonce", self.guest1.fav_song)
    
    