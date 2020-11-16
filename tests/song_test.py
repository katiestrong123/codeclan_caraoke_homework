# import unittest
# from tests.guest_test import *
# from tests.room_test import *
# from tests.song_test import *

import unittest
from classes.guest import *
from classes.room import *
from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Maggotbrain")
        self.song_2 = Song("Sweet Thang")
        self.song_3 = Song("Gold Snafu")

    def test_song_has_name(self):
        self.assertEqual("Maggotbrain", self.song_1.name)


