import requests 
from bs4 import BeautifulSoup
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

class Artist:
    def __init__(self, name, uri, image, festival):
        self.name = name
        self.uri = uri
        self.image = 'No image'
        self.festival = festival

    def __str__(self):
        return f'{self.name}, {self.uri}, {self.image}, {self.festival}'

class ArtistManager():
    def __init__(self):
        self.festivalartists = []

    def roskilde_festival(self):
        result = requests.get("https://www.roskilde-festival.dk/en/line-up/") 
        c = result.content
        soup = BeautifulSoup(c, 'xml')
        samples = soup.find_all("a", "name")
        dump = [] #Added momentarily storage, as the generator object is not subscriptable
        for artist in samples:
            dump.append(list(artist.stripped_strings)[0])
        for x in dump: 
            self.festivalartists.append(x)

    def __str__(self):
        return str(self.festivalartists)

class SpotifyData():
    def __init__(self):
        self.artistobjects = []
        self.roskildefestival = []
        self.listoflists = []

    def get_data(self, artist_manager):
        client_credentials_manager = SpotifyClientCredentials(client_id='1fc1953f35974811bb2511e360dd422b', client_secret='172b85d4d592449f9268ab7285598088')
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        for element in artist_manager.festivalartists:
            if len(sys.argv) > 1:
                name = ' '.join(sys.argv[1:])
            else:
                name = element
                results = spotify.search(q='artist:' + name, type='artist')
                items = results['artists']['items']
                if len(items) > 0:
                    artist = items[0]
                    artist_object_data = list((artist['name'], artist['external_urls']['spotify']))
                    uppermatch = artist_object_data[0].upper() #This could perhaps be done smarter
                    if uppermatch != element:
                        self.listoflists.append([element,'Not on Spotify'])
                    self.listoflists.append(artist_object_data)

    def initialize_artist(self):
        for element in self.listoflists:
            artist_name = element[0]
            artist_uri = element[1]
            new_artist = Artist(artist_name, artist_uri,'','Roskilde Festival')
            self.artistobjects.append(new_artist)

    #Prints Artist objects
    def print_artistobjects(self):
        for x in self.artistobjects:
            print(x)

ArtistManager = ArtistManager()
SpotifyData = SpotifyData()

# Request data + append artists to list
ArtistManager.roskilde_festival()

#Get spotify data from queeries via artistlist
SpotifyData.get_data(ArtistManager)

#Initialize artist objects via spotify data
SpotifyData.initialize_artist()

#Prints artist objects
SpotifyData.print_artistobjects()

# add images + additional data
# integrate with other repo
# add db integration