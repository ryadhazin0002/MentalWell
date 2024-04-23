import pygame
from pygame import mixer
import os
from pytube import YouTube


class Music:
    def __init__(self):
        # TODO add pygame.init()
        mixer.init()
        self.music = mixer.music
        self.song_collection = SongCollection()
        self.path = self.song_collection.musicPath[0]

        self.music.set_endevent(pygame.USEREVENT)

        self.music_end = pygame.USEREVENT + 1  # set event

    def load_music(self):
        self.music.load(self.path)

    def play_music(self):
        self.music.play()

    def stop_music(self):
        end_event_type = self.music.get_endevent()

        print("stopped")
        self.music.stop()

    def change_music(self, num):
        self.path = self.song_collection.musicPath[num]


class SongCollection:
    def __init__(self):
        self.folder = '.\\Music'  # Location of stores songs
        self.musicPath = []  # Use this to play songs
        self.create_list()

    def create_list(self):
        song_path = os.listdir(self.folder)
        for i in song_path:
            self.musicPath.append(f'{self.folder}' + '\\' + i)


class DownloadSongs:
    @staticmethod
    def download(link):
        yt = YouTube(link)
        if "youtube" not in link:
            return  # wrong link return nothing
        audio = yt.streams.filter(only_audio=True).first()
        out_file = audio.download(output_path="Music")
        base, ext = os.path.splitext(out_file)
        new_mp3_file = base + ".mp3"
        os.rename(out_file, new_mp3_file)


pygame.init()
MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)
mixer.init()

musicc = mixer.music
musicc.load(".\\Music\\testSound.mp3")
musicc.play()

while True:
    for event in pygame.event.get():
        if pygame.mixer.music.get_endevent() == MUSIC_END and not pygame.mixer.music.get_busy():
            musicc.stop()
            print("Music stopped")

    next_song = input("Next song? Y/N")

    if next_song == "Y":
        musicc.stop()
        musicc.load(".\\Music\\Bosun Bill.mp3")
        musicc.play()

a = input("wait: ")
if a:
    pass

pygame.mixer.music.get_endevent()
print("Test if music ends")

# TESTING
# music = Music()
# music.load_music()
# music.play_music()
#
# inputkey = input("input")
# if inputkey == "s":
#     music.stop_music()
#
#

# import pygame
# import pygame.locals
#
# pygame.init()
# pygame.mixer.init()
#
# # Load music
# pygame.mixer.music.load('.\\Music\\testSound.mp3')
#
# # Set an event to be triggered when the music ends
# pygame.mixer.music.set_endevent(pygame.locals.USEREVENT)
#
# # Start playing the music
# pygame.mixer.music.play()

# Get the event type for music end
# end_event_type = pygame.mixer.music.get_endevent()
#
# print("Event type for music end:", end_event_type)

# Main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.locals.QUIT:
#             running = False
#         elif event.type == end_event_type:
#             print("Music ended!")
#


# Add any code you want to execute when the music ends

# pygame.quit()
