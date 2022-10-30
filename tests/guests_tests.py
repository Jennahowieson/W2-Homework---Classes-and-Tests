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
        self.song1 = Song("beyonce", 3)
        self.song2 = Song("britney", 2)
    
    def test_guest_has_money(self):
        self.assertEquals (15, self.guest1.money)

    def test_guest_has_fave_song(self):
        self.assertEquals ("beyonce", self.guest1.fav_song)
    
    def test_cheer_fav_song(self):
        self.bar.check_in_guest(self.guest1)
        self.bar.check_in_song(self.song1)
        song_to_check = self.guests.cheer_fav_song(self.song1, self.guest1)
        self.assertEquals ("Yay, my favourite song is in the room", song_to_check)