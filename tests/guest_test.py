# import unittest
# from tests.room_test import *
# from tests.song_test import *
# from tests.guest_test import *

import unittest
from classes.guest import *
from classes.room import *
from classes.song import *


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Cassia Briscoe", 27, "Gold Snafu", 100)

    def test_guest_has_name(self):
        self.assertEqual("Cassia Briscoe", self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(27, self.guest_1.age)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Gold Snafu", self.guest_1.favourite_song)

    def test_guest_has_money(self):
        self.assertEqual(100, self.guest_1.cash)


    def test_guest_can_afford__True(self):
        self.assertEqual(True, self.guest_1.guest_can_afford(10))

    def test_guest_can_afford__False(self):
        self.assertEqual(False, self.guest_1.guest_can_afford(1000))
    
    def test_guest_can_buy_drink__True(self):
        self.assertEqual("Yas Kween, get krunk", self.guest_1.can_buy_drink(self.guest_1))

    def test_reduce_wallet(self):
        self.assertEqual(90, self.guest_1.reduce_wallet(10))
