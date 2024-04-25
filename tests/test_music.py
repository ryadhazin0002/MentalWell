import unittest
import src.music
from src.music import SongCollection


class testMusic(unittest.TestCase):
    def setUp(self):
        self.music = src.music.Music()
        self.aandres = "..\\Music\\AAndres_Song.mp3"
        self.aerie = "..\\Music\\Aerie.mp3"
        self.cat = "..\\Music\\C418 - Cat - Minecraft Volume Alpha.mp3"
        self.dog = "..\\Music\\C418 - Dog - Minecraft Volume Alpha.mp3"
        self.droopy = "..\\Music\\C418 - Droopy likes Ricochet - Minecraft Volume Alpha.mp3"
        self.dry_hands = "..\\Music\\C418 - Dry Hands - Minecraft Volume Alpha.mp3"
        self.haggstrom = "..\\Music\\C418 - Haggstrom - Minecraft Volume Alpha.mp3"
        self.mice = "..\\Music\\C418 - Living Mice - Minecraft Volume Alpha.mp3"
        self.mice_venus = "..\\Music\\C418 - Mice on Venus - Minecraft Volume Alpha.mp3"
        self.minecraft = "..\\Music\\C418 - Minecraft - Minecraft Volume Alpha.mp3"
        self.moog_city = "..\\Music\\C418 - Moog City - Minecraft Volume Alpha.mp3"
        self.sweden = "..\\Music\\C418 - Sweden - Minecraft Volume Alpha.mp3"
        self.wet_hands = "..\\Music\\C418 - Wet Hands - Minecraft Volume Alpha.mp3"
        self.firebugs = "..\\Music\\Firebugs.mp3"
        self.moog_city_2 = "..\\Music\\Minecraft Volume Beta - Moog City 2.mp3"


    def teardown(self):
        self.music = src.music.Music()
        self.aandres = "..\\Music\\AAndres_Song.mp3"
        self.aerie = "..\\Music\\Aerie.mp3"
        self.cat = "..\\Music\\C418 - Cat - Minecraft Volume Alpha.mp3"
        self.dog = "..\\Music\\C418 - Dog - Minecraft Volume Alpha.mp3"
        self.droopy = "..\\Music\\C418 - Droopy likes Ricochet - Minecraft Volume Alpha.mp3"
        self.dry_hands = "..\\Music\\C418 - Dry Hands - Minecraft Volume Alpha.mp3"
        self.haggstrom = "..\\Music\\C418 - Haggstrom - Minecraft Volume Alpha.mp3"
        self.mice = "..\\Music\\C418 - Living Mice - Minecraft Volume Alpha.mp3"
        self.mice_venus = "..\\Music\\C418 - Mice on Venus - Minecraft Volume Alpha.mp3"
        self.minecraft = "..\\Music\\C418 - Minecraft - Minecraft Volume Alpha.mp3"
        self.moog_city = "..\\Music\\C418 - Moog City - Minecraft Volume Alpha.mp3"
        self.sweden = "..\\Music\\C418 - Sweden - Minecraft Volume Alpha.mp3"
        self.wet_hands = "..\\Music\\C418 - Wet Hands - Minecraft Volume Alpha.mp3"
        self.firebugs = "..\\Music\\Firebugs.mp3"
        self.moog_city_2 = "..\\Music\\Minecraft Volume Beta - Moog City 2.mp3"

    def test_change_song(self):
        self.music.change_song(-2)
        self.assertEqual(self.music.current_song, self.firebugs)
        self.music.change_song(-1)
        self.assertEqual(self.music.current_song, self.moog_city_2)
        self.music.change_song(2)
        self.assertEqual(self.music.current_song, self.cat)
        self.music.change_song(3)
        self.assertEqual(self.music.current_song, self.dog)

    def test_next_song(self):
        self.music.change_song(-2)
        self.assertEqual(self.music.current_song, self.firebugs)
        self.music.next_song()
        self.assertEqual(self.music.current_song, self.moog_city_2)
        self.music.next_song()
        self.assertEqual(self.music.current_song, self.aandres)
        self.music.next_song()
        self.assertEqual(self.music.current_song, self.aerie)

    def test_prev_song(self):
        self.music.change_song(0)
        self.assertEqual(self.music.current_song, self.aandres)
        self.music.prev_song()
        self.assertEqual(self.music.current_song, self.moog_city_2)
        self.music.prev_song()
        self.assertEqual(self.music.current_song, self.firebugs)
        self.music.prev_song()
        self.assertEqual(self.music.current_song, self.wet_hands)


class TestMusicCollection(unittest.TestCase):
    def setUp(self):
        self.musicPath = SongCollection().musicPath
        self.music = src.music.Music()
        self.aandres = "..\\Music\\AAndres_Song.mp3"
        self.aerie = "..\\Music\\Aerie.mp3"
        self.cat = "..\\Music\\C418 - Cat - Minecraft Volume Alpha.mp3"
        self.dog = "..\\Music\\C418 - Dog - Minecraft Volume Alpha.mp3"
        self.droopy = "..\\Music\\C418 - Droopy likes Ricochet - Minecraft Volume Alpha.mp3"
        self.dry_hands = "..\\Music\\C418 - Dry Hands - Minecraft Volume Alpha.mp3"
        self.haggstrom = "..\\Music\\C418 - Haggstrom - Minecraft Volume Alpha.mp3"
        self.mice = "..\\Music\\C418 - Living Mice - Minecraft Volume Alpha.mp3"
        self.mice_venus = "..\\Music\\C418 - Mice on Venus - Minecraft Volume Alpha.mp3"
        self.minecraft = "..\\Music\\C418 - Minecraft - Minecraft Volume Alpha.mp3"
        self.moog_city = "..\\Music\\C418 - Moog City - Minecraft Volume Alpha.mp3"
        self.sweden = "..\\Music\\C418 - Sweden - Minecraft Volume Alpha.mp3"
        self.wet_hands = "..\\Music\\C418 - Wet Hands - Minecraft Volume Alpha.mp3"
        self.firebugs = "..\\Music\\Firebugs.mp3"
        self.moog_city_2 = "..\\Music\\Minecraft Volume Beta - Moog City 2.mp3"

    def tearDown(self):
        self.musicPath = SongCollection().musicPath
        self.music = src.music.Music()
        self.aandres = "..\\Music\\AAndres_Song.mp3"
        self.aerie = "..\\Music\\Aerie.mp3"
        self.cat = "..\\Music\\C418 - Cat - Minecraft Volume Alpha.mp3"
        self.dog = "..\\Music\\C418 - Dog - Minecraft Volume Alpha.mp3"
        self.droopy = "..\\Music\\C418 - Droopy likes Ricochet - Minecraft Volume Alpha.mp3"
        self.dry_hands = "..\\Music\\C418 - Dry Hands - Minecraft Volume Alpha.mp3"
        self.haggstrom = "..\\Music\\C418 - Haggstrom - Minecraft Volume Alpha.mp3"
        self.mice = "..\\Music\\C418 - Living Mice - Minecraft Volume Alpha.mp3"
        self.mice_venus = "..\\Music\\C418 - Mice on Venus - Minecraft Volume Alpha.mp3"
        self.minecraft = "..\\Music\\C418 - Minecraft - Minecraft Volume Alpha.mp3"
        self.moog_city = "..\\Music\\C418 - Moog City - Minecraft Volume Alpha.mp3"
        self.sweden = "..\\Music\\C418 - Sweden - Minecraft Volume Alpha.mp3"
        self.wet_hands = "..\\Music\\C418 - Wet Hands - Minecraft Volume Alpha.mp3"
        self.firebugs = "..\\Music\\Firebugs.mp3"
        self.moog_city_2 = "..\\Music\\Minecraft Volume Beta - Moog City 2.mp3"

    def test_first_item(self):
        self.assertEqual(self.musicPath[0], self.aandres)

    def test_second_item(self):
        self.assertEqual(self.musicPath[1], self.aerie)

    def test_third_item(self):
        self.assertEqual(self.musicPath[2], self.cat)

    def test_fourth_item(self):
        self.assertEqual(self.musicPath[3], self.dog)

    def test_fifth_item(self):
        self.assertEqual(self.musicPath[4], self.droopy)

    def test_sixth_item(self):
        self.assertEqual(self.musicPath[5], self.dry_hands)

    def test_seventh_item(self):
        self.assertEqual(self.musicPath[6], self.haggstrom)

    def test_eighth_item(self):
        self.assertEqual(self.musicPath[7], self.mice)

    def test_ninth_item(self):
        self.assertEqual(self.musicPath[8], self.mice_venus)

    def test_tenth_item(self):
        self.assertEqual(self.musicPath[9], self.minecraft)

    def test_eleventh_item(self):
        self.assertEqual(self.musicPath[10], self.moog_city)

    def test_twelfth_item(self):
        self.assertEqual(self.musicPath[11], self.sweden)

    def test_thirteenth_item(self):
        self.assertEqual(self.musicPath[12], self.wet_hands)

    def test_fourteenth_item(self):
        self.assertEqual(self.musicPath[13], self.firebugs)

    def test_fifteenth_item(self):
        self.assertEqual(self.musicPath[14], self.moog_city_2)


if __name__ == '__main__':
    unittest.main()
