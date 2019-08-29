import requests 
from bs4 import BeautifulSoup
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import mysql.connector 

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

class SpotifyData():
    def __init__(self):
        self.artistobjects = []
        self.listoflists = []
        self.new_list = []
        
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

    def artisttuple(self):
        self.new_list = list(map(lambda x: (x.name, x.uri, x.image, x.festival), self.artistobjects))

class DbConnect():
    def __init__(self):
        pass

    def connect(self, data):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="festivalg"
        )
        mycursor = mydb.cursor()
        query = "INSERT INTO roskildefestival (name, image, url, festival) VALUES (%s, %s, %s, %s)"
        mycursor.executemany(query, data.new_list)
        mydb.commit()
        print(mycursor.rowcount, "was inserted.")
        
#Define classes as variables
ArtistManager = ArtistManager()
SpotifyData = SpotifyData()
DbConnect = DbConnect()

# Request data + append artists to list
ArtistManager.roskilde_festival()

#Get spotify data from queries via artistlist
SpotifyData.get_data(ArtistManager)

#Initialize artist objects via spotify data
SpotifyData.initialize_artist()

#Rewrites artistobjects into tuple, that can be appended to db
SpotifyData.artisttuple()

#Append spotify data to db
DbConnect.connect(SpotifyData)

#2. add image to data
#3. integrate with exsisting repo