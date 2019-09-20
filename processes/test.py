from bs4 import BeautifulSoup 
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
from app import db
from models import Artist

#Storage of artist names before running appending data through spotify query
class FestivalScraper():
    def __init__(self):
        self.artists = []
  
    #Artists from roskilde festival
    def roskildescraper(self):
        content = requests.get('https://www.roskilde-festival.dk/en/line-up/')
        soup = BeautifulSoup(content.text, 'html.parser')
        data = soup.find_all('a','name')
        for artist in data:
            artistlist = [next(artist.stripped_strings), 'Roskilde Festival']
            self.artists.append(artistlist) 
  
    #Artists from smukfest
    def smukfestscraper(self):
        content = requests.get('https://www.smukfest.dk/musik/spilleplan-2019')
        soup = BeautifulSoup(content.text, 'html.parser')
        data = soup.find_all('a','schedule__act-link')
        for artist in data:
            artistlist = [next(artist.stripped_strings), 'Smuk Fest']
            self.artists.append(artistlist) 

#Using previous scraped data for spotify queries.
# Storing them as a list of dictionaries, to easier append to postgres/sqlalchemy 
class SpotifyData():
    def __init__(self):
        self.artistobjects = []

    def getdata(self, artistdata):
        client_credentials_manager = SpotifyClientCredentials(client_id='1fc1953f35974811bb2511e360dd422b', client_secret='172b85d4d592449f9268ab7285598088')
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        for sub_list in artistdata.artists:
            artistdict = {}
            artistdict['Name'] = sub_list[0]
            artistdict['Festival'] = sub_list[1]
            try:
                results = spotify.search(q='artist:' + sub_list[0], type='artist')
                if len(results) > 0:
                    items = results['artists']['items']
                    if len(items) > 0:
                        artist = items[0]
                        image = artist['images'][0]['url']
                        if len(image) > 0:
                            artistdict['Image'] = image
                        else:
                            artistdict['Image'] = 'Not avaliable'  
                        uri = artist['external_urls']['spotify']
                        if len(uri) > 0:
                            artistdict['Uri'] = uri
                        else:
                            artistdict['Uri'] = 'Not avaliable'  
                        self.artistobjects.append(dict(artistdict))
            except:
                artistdict['Image'] = 'Not avaliable'
                artistdict['Uri'] = 'Not avaliable'
                self.artistobjects.append(dict(artistdict))
        

#Define classes as variables
FestivalScraper = FestivalScraper()
SpotifyData = SpotifyData()
#Populate artist names to lists depending on their festival
FestivalScraper.roskildescraper()
FestivalScraper.smukfestscraper()
SpotifyData.getdata(FestivalScraper)

#For testing
print(SpotifyData.artistobjects)


#Db session
for artistdict in SpotifyData.artistobjects:
    artist = Artist(**artistdict)
    db.session.add(artist)
    db.session.commit()

