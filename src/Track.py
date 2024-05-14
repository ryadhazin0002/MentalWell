# DB for music
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

