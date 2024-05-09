import pygame
import os
import threading


class MusicPlayer:
    pygame.init()
    music = pygame.mixer.music
    songs = []
    play_button = False
    auto_play_thread = True
    create_thread = True  # Creates 1 thread that lasts the time program runs... deleting and recreating causes issues
    song_tracker = 0
    END_OF_SONG = pygame.USEREVENT + 1


    @classmethod
    def play_logic(cls):
        match cls.play_button:
            case False:
                cls.play_music()
            case True:
                if cls.music.get_busy() is True:
                    cls.music.pause()
                else:
                    cls.music.unpause()


    @classmethod
    def play_music(cls):
        if cls.play_button is False:
            cls.play_button = True
            cls.auto_play_thread = True
        if cls.create_thread is True:
            cls.activate_thread()

        cls.music.load(cls.songs[cls.song_tracker])
        cls.music.play()
        cls.music.set_endevent(cls.END_OF_SONG)


    @classmethod
    def stop_music(cls):  # Exits the window SHOULD stop thread too
        cls.play_button = False
        cls.auto_play_thread = False
        cls.music.stop()


    @classmethod
    def change_song(cls, num):
        cls.song_tracker = num
        cls.music.load(cls.songs[cls.song_tracker])
        cls.play_music()


    @classmethod
    def next_song(cls):
        cls.song_tracker += 1
        cls.update_song()


    @classmethod
    def prev_song(cls):
        cls.song_tracker -= 1
        cls.update_song()


    @classmethod
    def update_song(cls):
        cls.song_tracker %= len(cls.songs)
        cls.play_music()


    @classmethod
    def auto_skip(cls):
        while True:
            while cls.auto_play_thread:
                if cls.music.get_busy() is False:
                    for _ in pygame.event.get():
                        if cls.music.get_endevent() == cls.END_OF_SONG and not cls.music.get_busy():
                            cls.next_song()
                            print("Next song")


    @classmethod
    def activate_thread(cls):
        cls.create_thread = False
        end_song_thread = threading.Thread(target=cls.auto_skip, daemon=True)
        end_song_thread.start()


    @classmethod
    def load_song_path(cls):
        folder = '..\\Music'
        for i in os.listdir(folder):
            cls.songs.append(f'{folder}\\{i}')
