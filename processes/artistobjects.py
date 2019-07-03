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
mycursor.execute("SELECT * FROM roskildeartists LIMIT 1") #Selects first item from table (w. name alkymist)
myresult = mycursor.fetchall() #Fetch all elements from Mysql Database

#For element in result (Inserted in SpotifyApi query further down)
for artist in myresult:
  print(repr(artist)) #This element should be put into "name" in spotipy

#Import libraries for spotipy
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

#Spotify: Client Creditial flow (client_id + client_secret)
client_credentials_manager = SpotifyClientCredentials(client_id='1fc1953f35974811bb2511e360dd422b', client_secret='172b85d4d592449f9268ab7285598088')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Get album data from first row in table (test)
if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = str(artist) #Inserts SQL query result here

#Search spotify with query (q) with artist name, and retrieves name,image,uri,genres in list
results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    artist_object_data = list(([artist['name']], [artist['images'][0]['url']], [artist['external_urls']['spotify']], artist['genres']))
    print(repr(artist_object_data))


#INSERT DATA INTO TABLE (INSERT / UPDATE DATA) (QUERY)
    #Overwrite name (UPDATE) (makes it case-sensitive)
    #Insert image (INSERT)
    #Insert external url (INSERT)
    #Insert genres (INSERT)

#FURTHER FEATURES TO IMPLEMENT
    #Get artist top tracks (requires user authentication)
    #get artist Festival (Look at sql table(or column in table) where name was taken from)

# ISSUES
    #Only retrieve value from external_urls
    #IF NO SPOTIFY LINK EXSIST DO: ??
    #DON't STORE DATA IF VALUES ALREADY EXSIST

#SNIPPET FOR TOPTRACKS (NEEDS AUTHENTICATION)
#Converts URL to string, for making request for top tracks further down
# for i in artist_object_data[2]:
#     print(i, end="")


# lz_uri = str(artist_object_data[2]) #Insert query found in Earlier API Request
#
# spotify = spotipy.Spotify()
# results = spotify.artist_top_tracks(lz_uri)
#
# for track in results['tracks'][:10]:
#     print('track : ' + track['name'])
#     print('track : ' + track['name'])
#     print('audio : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
