import unittest
from classes.bar import *
from classes.guests import *
from classes.songs import *
from classes.room import *

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("beyonce", 3)
    
    def test_song_has_name(self):
        self.assertEquals ("beyonce", self.song1.name)

    def test_song_has_duration(self):
        self.assertEquals (3, self.song1.duration)
    