class Room:
    def __init__(self, name, song_selection, till):
        self.name = name
        self.song_selection = song_selection
        self.till = till
        self.guests = []
    
    def count_guests(self):
        return len(self.guests)

    def add_guest_to_room(self, guest_to_add):
        if len(self.guests) > 3:
            return "Sorry mate, we're at capacity"
        self.guests.append(guest_to_add)

    def remove_guest_from_room(self, guest_to_remove):
        self.guests.remove(guest_to_remove)

    def count_song_list(self):
        return len(self.song_selection)

    def add_song(self, song_to_add):
        self.song_selection.append(song_to_add)
        return len(self.song_selection)

    def increase_till(self, amount):
        self.till += amount
        return self.till

    # def take_room_charge(self, guest_paying, room_charge):
    #     self.increase_till(rooom_charge)
    #     guest.guest_paying.reduce_wallet(rooom_charge)