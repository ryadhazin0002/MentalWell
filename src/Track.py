# DB for music
from src.connect_to_database import DatabaseManager


class Track:
    def __init__(self, id, name, author, musicPath, imagePath) -> None:
        self.id = id
        self.name = name
        self.author = author
        self.musicPath = musicPath
        self.imagePath = imagePath


    id: int
    name: str
    author: str
    musicPath: str
    imagePath: str

class TrackFunctions:

    tracks: list[Track]
    current_quote_index = None

    def __init__(self) -> None:
        self.database = DatabaseManager()
        self.tracks = self.getAll()
        self.set_current_track(0)
        pass

    def set_current_track(self, index)-> Track:
        if index < len(self.tracks):
            self.current_track_index = index
            return self.tracks[index]


    def getAll(self) -> list[Track]:
        result = self.database.execute_query("Select * from music_list;")
        if result != None:
            data = []
            for item in result:
                data.append(Track(item[0], item[1], item[2], item[3], item[4]))
            return data
        return []

    def next_track(self)-> Track:
        if self.current_track_index != len(self.tracks)-1:
            return self.set_current_track(self.current_track_index+1)
        else:
            first_song = 0
            return self.set_current_track(first_song)

    def previous_track(self)-> Track:
        if self.current_track_index != 0:
            return self.set_current_track(self.current_track_index-1)
        else:
            last_song = len(self.tracks)-1
            return self.set_current_track(last_song)

    def current_track(self):
        if self.current_track_index is None:
            return None
        return self.tracks[self.current_track_index]
