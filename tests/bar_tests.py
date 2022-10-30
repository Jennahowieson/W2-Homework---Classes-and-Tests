import unittest
from classes.bar import *
from classes.guests import *
from classes.songs import *
from classes.room import *

class TestBar(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest(15, "beyonce", False)
        self.guest2 = Guest(20, "beyonce", False)
        self.guest3 = Guest(10, "britney", False)
        
        guests = [self.guest1, self.guest2, self.guest3]

        self.song1 = Song("beyonce", 3)
        self.song2 = Song("britney", 2)
        songs=[self.song1, self.song2]
        
        self.bar = Bar(15, guests, songs, 20)

    def test_bar_capacity(self):
        self.assertEqual(15, self.bar.capacity)
    
    def test_check_in_guests(self):
        guest_status = self.bar.check_in_guest(self.guest1)
        self.assertEquals(True,self.guest1.status)

    def test_num_current_guests(self):
        self.bar.check_in_guest(self.guest1)
        current_guests = self.bar.get_current_guests()
        self.assertEquals(1,len(current_guests))
    
    def test_check_in_song (self):
        song_status = self.bar.check_in_song(self.song1)
        self.assertEquals(True,self.song1.status)
    
    def test_check_out_song (self):
        self.bar.check_in_song(self.song2)
        self.bar.check_out_song(self.song2)
        self.assertEquals(False,self.song2.status)

    def test_add_song_to_room(self):
        self.bar.check_in_song(self.song1)
        self.bar.check_in_song(self.song2)
        songs_in_room = self.bar.get_current_songs()
        self.assertEquals(2, len(songs_in_room))
    
    def test_cheer_fav_song(self):
        self.bar.check_in_guest(self.guest1)
        self.bar.check_in_song(self.song1)
        song_to_cheer = self.guest1.cheer_fav_song(self.guest1)
        self.assertEquals ("Yay, my favourite song is in the room", song_to_cheer)