

class Guest:
    def __init__(self, money, fav_song, status):
        self.money = money
        self.fav_song = fav_song
        self.status = status
    
    def find_fave_song(self,guest):
        for guest in guest:
            return self.guest.fave_song
    
    def cheer_fav_song(self,guest):
        song_to_cheer = self.find_fave_song(guest)
        if song_to_cheer.song.status == True and guest.status== True:
            return "Yay, my favourite song is in the room" 
        else:
            return "Boo, I want my song"
