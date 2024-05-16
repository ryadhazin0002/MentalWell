import time

import pygame
import os
import threading

from config import music_path
from src.Track import TrackFunctions


class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.music = pygame.mixer.music
        self.track_functions = TrackFunctions()
        self.songs = []
        self.play_button = False
        self.auto_play_thread = True
        self.song_tracker = 0
        self.END_OF_SONG = pygame.USEREVENT + 1
        self.load_song_path()
        self.end_song_thread = threading.Thread(target=self.auto_skip, daemon=True)
        self.end_song_thread.start()




    def play_logic(self):
        match self.play_button:
            case False:
                self.play_music()

            case True:
                if self.music.get_busy() is True:
                    self.music.pause()
                else:
                    self.music.unpause()


    def play_music(self):
        if self.play_button is False:
            self.play_button = True
            self.auto_play_thread = True

        self.music.load(self.songs[self.song_tracker])
        self.music.play()
        self.music.set_endevent(self.END_OF_SONG)




    def change_song(self, num):
        self.song_tracker = num
        self.music.load(self.songs[self.song_tracker])
        self.play_music()


    def next_song(self):
        self.song_tracker += 1
        self.update_song()


    def prev_song(self):
        self.song_tracker -= 1
        self.update_song()


    def update_song(self):
        self.song_tracker %= len(self.songs)
        self.play_music()


    def auto_skip(self):
        while True:
            while self.auto_play_thread:
                for _ in pygame.event.get():
                    if self.music.get_endevent() == self.END_OF_SONG and not self.music.get_busy():
                        self.next_song()
                        print("Next song")

    def is_playing(self):
        """
        Check if music is currently playing.
        Returns:
            bool: True if music is playing, False otherwise.
        """
        return self.music.get_busy()


    def load_song_path(self):
        #folder = music_path
        for i in self.track_functions.tracks:
            self.songs.append(i.musicPath)
        #for i in os.listdir(folder):
            #self.songs.append(f'{folder}\\{i}')
