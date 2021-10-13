class MusicBand:
    def __init__(self, title, label, musician=None):
        self.title = title
        self.label = label
        
        self.musician = musician

        self.album = []


    def write_album(self, album):
        self.album.append(album)


class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
    
    def __str__(self):
        return f"{self.name} {self.instrument}"

class Album:
    def __init__(self, song, genre):
        self.song = song
        self.genre = genre


band1 = MusicBand("The Beatles", "Parlophone", "beatles")
band1.write_album("White Album")
band1.write_album("Hard Day's Night")
band1.write_album("Help")

print(band1.title, band1.musician, band1.label, band1.album)

