from bs4 import BeautifulSoup 
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
from app import db
from app import Artist

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
# Storing them as a list of dictionaries, to easier append with Sqlalchemy(ORM) 
class SpotifyData():
    def __init__(self):
        self.artistobjects = []

    def getdata(self, artistdata):
        client_credentials_manager = SpotifyClientCredentials(client_id='1fc1953f35974811bb2511e360dd422b', client_secret='172b85d4d592449f9268ab7285598088')
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        #For list in webscraper, append names to dict
        for artists in artistdata.artists:
            artistdict = {}
            artistdict['name'] = artists[0]
            #Spotify query on artistname
            results = spotify.search(q='artist:' + artists[0], type='artist')
            #Check if query returns true (will still return true if 401, and no data though)
            if results:
                items = results['artists']['items']
                #Check if spotify data exsists for artist
                if items:
                    try:
                        artistdict['img'] = items[0]['images'][0]['url']
                    except:
                        artistdict['img'] = '../static/img/unknown.jpg'
                    try:
                        artistdict['uri'] = items[0]['external_urls']['spotify']
                    except:
                        artistdict['uri'] = 'None'
                #If no spotify data is found on the name provided from webscraper list append none-values
                else:
                    artistdict['img'] = '../static/img/unknown.jpg'
                    artistdict['uri'] = 'None'
            # Append related festival from scraped data to dict        
            artistdict['festival'] = artists[1]
            #Append artist dict to list     
            self.artistobjects.append(dict(artistdict))

#Define classes as variables
FestivalScraper = FestivalScraper()
SpotifyData = SpotifyData()
#Populate artist names to lists depending on their festival
FestivalScraper.roskildescraper()
FestivalScraper.smukfestscraper()
SpotifyData.getdata(FestivalScraper)
#Append artistobjects to db
for artistdict in SpotifyData.artistobjects:
    artist = Artist(**artistdict)
    db.session.add(artist)
    db.session.commit()




