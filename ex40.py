class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):

        for line in self.lyrics:
            print line

    def sing_me_more(self, n = 2):
        n_lyrics = self.lyrics * n

        for line in n_lyrics:
            print line

class Pop_song(Song):
    def __init__(self, lyrics):
        self.lyrics = lyrics



happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "Wiht pockets full of shells"])

country_road = Pop_song(["Country road",
                     "Take me home"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
country_road.sing_me_a_song()

country_road.sing_me_more()
bulls_on_parade.sing_me_more(3)
