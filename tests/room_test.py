import unittest
from classes.guest import *
from classes.room import *
from classes.song import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        song_selection = ["Hot Jazzybelle", "Tell Me Are We", "Talk to Me You'll Understand"]

        self.song_2 = "195"

        self.room = Room("Dance Dance Room", song_selection, 1000)

        self.guest_1 = Guest("Kia Tansley", 25, "Hot Jazzybelle", 50)
        self.guest_2 = Guest("Lulu Roberts", 23, "Savage", 20)
        self.guest_3 = Guest("Faye Anderson", 22, "Jet Fuel", 60)
        self.guest_4 = Guest("Pia Baraldi", 25, "Hardest Button To Button", 30)

    def test_room_has_name(self):
        self.assertEqual("Dance Dance Room", self.room.name)
    
    def test_room_has_song_selection(self):
        self.assertEqual(["Hot Jazzybelle", "Tell Me Are We", "Talk to Me You'll Understand"], self.room.song_selection)

    def test_guests_is_empty(self):
        self.assertEqual(0, self.room.count_guests())

    def test_can_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest_1)
        self.assertEqual(1, self.room.count_guests())

    def test_count_song_list(self):
        self.assertEqual(3, self.room.count_song_list())

    def test_can_remove_guest_from_room(self):
        self.room.add_guest_to_room(self.guest_1)
        self.room.remove_guest_from_room(self.guest_1)
        self.assertEqual(0, self.room.count_guests())

    def test_can_add_song(self):
        self.room.add_song(self.song_2)
        self.assertEqual(['Hot Jazzybelle', 'Tell Me Are We', "Talk to Me You'll Understand", '195'], self.room.song_selection)

    def test_room_has_max_capacity(self):
        self.room.add_guest_to_room(self.guest_1)
        self.room.add_guest_to_room(self.guest_2)
        self.room.add_guest_to_room(self.guest_3)
        self.room.add_guest_to_room(self.guest_4)
        self.assertEqual("Sorry mate, we're at capacity", self.room.add_guest_to_room(self.guest_4))

    def tease_can_increase_till(self):
        self.assertEqual(1010, self.room.increase_till(10))
    