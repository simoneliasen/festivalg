#Get artist data from artist name (from db)
import mysql.connector #Import Mysql library

# Database credentials
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="festivalg"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM roskildeartists WHERE name = 'ALKYMIST' LIMIT 1") #Puts list into db, with each element being own list

myresult = mycursor.fetchall() #Fetch all elements from Mysql Database

for x in myresult: #For elements in results (insert element i query)
  print(repr(x))

#Import spotipy components
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

#Spotify: Client Creditial flow (client_id + client_secret)
client_credentials_manager = SpotifyClientCredentials(client_id='1fc1953f35974811bb2511e360dd422b', client_secret='172b85d4d592449f9268ab7285598088')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Get album Image from artist = ALKYMIST (test)
if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'ALKYMIST'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print (artist['name'], artist['images'][0]['url'])


#API Parameters
#artist(artist_id) #returns a single artist given the artist’s ID, URI or URL
#categories(country=None, locale=None, limit=20, offset=0) #Get artist country

# Data we want from artist name (creates artist object)
#- image (spotify API) (achievable)
#- description (spotifyAPI) (maybe not avaliable)
#- country (spotifyAPI) (achievable)
#- genre(spotifyAPI) (achievable)
#- toptracks(spotifyAPI) (achievable)
#- festivalplayingat(ParentClassFestival)

#Where to store artist object? semi permanently?
#Daily api gets? or every user request?
#What to do if data is not avaliable? (what if no spotify?) (what if no description?)

# #Get image URL of artist
# import spotipy
# import sys
#
# spotify = spotipy.Spotify()
#
# if len(sys.argv) > 1:
#     name = ' '.join(sys.argv[1:])
# else:
#     name = 'Radiohead'
#
# results = spotify.search(q='artist:' + name, type='artist')
# items = results['artists']['items']
#
# if len(items) > 0:
#     artist = items[0]
#     print artist['name'], artist['images'][0]['url']
#
#
# # Get top 10 tracks from artist
# import spotipy
#
# lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
#
# spotify = spotipy.Spotify()
# results = spotify.artist_top_tracks(lz_uri)
#
# for track in results['tracks'][:10]:
# print 'track : ' + track['name']
#     print 'track : ' + track['name']
#     print 'audio : ' + track['preview_url']
#     print 'cover art: ' + track['album']['images'][0]['url']
#     print
