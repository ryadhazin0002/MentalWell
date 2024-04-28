import os
import unittest
from src.music import Music
from src.music import SongCollection


class testMusic(unittest.TestCase):
    def setUp(self):
        self.music = Music()
        self.song_dir = "..\\Music\\"
        self.song_list = [self.song_dir + song for song in os.listdir(self.song_dir)]


    def teardown(self):
        self.music = Music()
        self.song_dir = "..\\Music\\"
        self.song_list = [self.song_dir + song for song in os.listdir(self.song_dir)]


    def test_change_song(self):
        for num, song in enumerate(self.song_list):
            self.music.change_song(num)
            self.assertEqual(song, self.music.current_song)


    def test_next_song(self):
        self.music.change_song(0)  # ensure to start from the beginning
        for i in range(len(self.song_list) + 5):  # + 5 makes it loop over and test the circular function
            self.assertEqual(self.song_list[i % len(self.song_list)], self.music.current_song)
            self.music.next_song()


    def test_prev_song(self):   # FIX IT
        self.music.change_song(-1)  # ensure to start from the end
        self.song_list.reverse()
        for i, song in enumerate(self.song_list):
            self.assertEqual(self.song_list[i % len(self.song_list)], self.music.current_song)
            self.music.prev_song()


class TestMusicCollection(unittest.TestCase):
    def setUp(self):
        self.musicPath = SongCollection().musicPath
        self.music = Music()
        self.song_dir = "..\\Music\\"
        self.song_list = [self.song_dir + song for song in os.listdir(self.song_dir)]


    def tearDown(self):
        self.musicPath = SongCollection().musicPath
        self.music = Music()
        self.song_dir = "..\\Music\\"
        self.song_list = [self.song_dir + song for song in os.listdir(self.song_dir)]


    def test_music_path_items(self):
        for i in range(len(self.song_list)):
            self.assertEqual(self.song_list[i], self.musicPath[i])


if __name__ == '__main__':
    unittest.main()