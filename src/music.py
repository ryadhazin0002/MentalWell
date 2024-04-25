import itertools

import pygame
from pygame import mixer
import os
from pytube import YouTube


class Music:
    def __init__(self):
        pygame.init()
        mixer.init()
        self.play_button = False
        self.music = mixer.music
        self.song_tracker = 0  # starts from first song
        self.song_collection = SongCollection()
        self.song_amount = len(self.song_collection.musicPath)
        self.current_song = self.song_collection.musicPath[self.song_tracker]
        self.END_OF_SONG = pygame.USEREVENT + 1


    def play_logic(self):  # initial button play
        match self.play_button:
            case False:
                self.play_song()
            case True:
                if self.music.get_busy() is True:
                    self.pause_song()
                else:
                    self.unpause_song()

    def play_song(self):
        self.music.load(self.current_song)
        self.music.play()
        self.play_button = True

    def stop_song(self):  # stop when click on main menu
        self.music.stop()


    def pause_song(self):  # pause on the play
        self.music.pause()


    def unpause_song(self):  # play on the play
        self.music.unpause()

    def change_song(self, num):  # DONE
        self.song_tracker = num
        self.music.load(self.current_song)
        self.current_song = self.song_collection.musicPath[self.song_tracker]


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


    def set_queue(self):  # queue should only be set 1 at the time?
        self.music.set_endevent(self.END_OF_SONG)


    def get_queue(self):
        for _ in pygame.event.get():
            if self.music.get_endevent() == self.END_OF_SONG and not self.music.get_busy():
                self.next_song()
                print("Next song")


class SongCollection:
    def __init__(self):
        self.folder = '.\\Music'  # Location of stores songs
        self.musicPath = []  # Use this to play songs
        itertools.cycle(self.musicPath)  # cycle to beginning at the end of list
        self.create_list()


    def create_list(self):
        song_path = os.listdir(self.folder)
        for i in song_path:
            self.musicPath.append(f'{self.folder}' + '\\' + i)


class DownloadSongs:  # Youtube change broke the library
    @staticmethod
    def download(link):
        if "https://www.youtube.com" not in link:
            print("Not a proper link")
            return  # wrong link return nothing

        yt = YouTube(link)
        audio = yt.streams.filter(only_audio=True).first()
        out_file = audio.download(output_path="Music")
        base, ext = os.path.splitext(out_file)
        new_mp3_file = base + ".MP3"
        os.rename(out_file, new_mp3_file)


    @staticmethod
    def provide_links():  # Automate download MP3 files from youtube
        while True:
            song_link = input("Enter Link: ")
            if song_link == "":
                break
            else:
                DownloadSongs.download(song_link)



