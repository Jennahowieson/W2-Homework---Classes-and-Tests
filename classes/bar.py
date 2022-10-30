class Bar:
    def __init__(self, capacity, guests, songs, fee):
        self.capacity = capacity
        self.guests = guests
        self.fee = fee
        self.songs = songs
    
    def check_in_guest(self,guest):
        guest.status = True
    
    def check_out_guest(self, guest):
        guest.status=False

    def get_current_guests(self):
        current_guests= []
        for guest in self.guests:
            if guest.status == True:
                current_guests.append(guest)
        return current_guests
    
    def check_in_song(self,song):
        song.status = True
    
    def check_out_song(self,song):
        song.status=False
    
    def get_current_songs(self):
        current_songs = []
        for song in self.songs:
            if song.status == True:
                current_songs.append(song)
        return current_songs