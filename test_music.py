import unittest.mock
from music import Song_Collection


class TestMusicCollection(unittest.TestCase):
    def setUp(self):
        self.musicPath = Song_Collection().musicPath


    def tearDown(self):
        self.musicPath = Song_Collection().musicPath


    def testFirstItem(self):
        self.assertEqual(self.musicPath[0], '.\\Music\\Bosun Bill.mp3')

    def testSecondItem(self):
        self.assertEqual(self.musicPath[1], ".\\Music\\Chopin - Nocturne op.9 No.2.mp3")

    def testThirdItem(self):
        self.assertEqual(self.musicPath[2], ".\\Music\\Sea of Thieves OST Music Soundtrack - 01 - Main Theme.mp3")

    def testFourthItem(self):
        self.assertEqual(self.musicPath[3], ".\\Music\\Tchaikovsky - Valse Sentimentale.mp3")


if __name__ == '__main__':
    unittest.main()
