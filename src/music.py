import pygame
import os
from pytube import YouTube
import threading


class Music:
    def __init__(self):
        pygame.init()
        self.play_button = False
        self.music = pygame.mixer.music
        self.song_tracker = 0  # starts from first song
        self.song_collection = SongCollection()
        self.song_amount = len(self.song_collection.musicPath)
        self.current_song = self.song_collection.musicPath[self.song_tracker]
        self.END_OF_SONG = pygame.USEREVENT + 1  # A queue ID for skipping songs

    def play_logic(self):  # initial button play
        match self.play_button:
            case False:
                self.play_song()
            case True:
                if self.music.get_busy() is True:
                    self.music.pause()
                else:
                    self.music.unpause()

    def play_song(self):
        if self.play_button is False:
            self.activate_thread()
            self.play_button = True

        self.music.load(self.current_song)
        self.music.play()
        self.music.set_endevent(self.END_OF_SONG)

    def stop_song(self):  # stop when click on main menu
        self.music.stop()

    def change_song(self, num):  # DONE
        self.song_tracker = num
        self.music.load(self.current_song)
        self.current_song = self.song_collection.musicPath[self.song_tracker]
        self.play_song()

    def next_song(self):  # DONE
        self.song_tracker += 1
        self.update_song()

    def prev_song(self):  # DONE
        self.song_tracker -= 1
        self.update_song()

    def update_song(self):  # DONE helper method
        self.song_tracker %= self.song_amount
        self.current_song = self.song_collection.musicPath[self.song_tracker]
        self.play_song()

    def song_ends(self):
        while True:
            if self.music.get_busy() is False:
                for _ in pygame.event.get():
                    if self.music.get_endevent() == self.END_OF_SONG and not self.music.get_busy():
                        self.next_song()
                        print("Next song")

    def activate_thread(self):
        end_song_thread = threading.Thread(target=self.song_ends, daemon=True)  # Auto skip song when it's done
        end_song_thread.start()  # Start thread to make it work


class SongCollection:
    def __init__(self):
        self.folder = '.\\Music'  # Location of stores songs
        self.musicPath = []  # Use this to play songs
        self.create_list()

    def create_list(self):
        song_path = os.listdir(self.folder)
        for i in song_path:
            self.musicPath.append(f'{self.folder}' + '\\' + i)
