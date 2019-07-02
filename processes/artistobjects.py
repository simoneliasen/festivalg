# Uses the name scraped with requests and beautifulSoup, to get artist info

# Get top 10 tracks from artist
import spotipy

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify()
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
print 'track : ' + track['name']
    print 'track : ' + track['name']
    print 'audio : ' + track['preview_url']
    print 'cover art: ' + track['album']['images'][0]['url']
    print


#Get image URL of artist
import spotipy
import sys

spotify = spotipy.Spotify()

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']

if len(items) > 0:
    artist = items[0]
    print artist['name'], artist['images'][0]['url']

#Parameters
artist(artist_id) #returns a single artist given the artist’s ID, URI or URL
categories(country=None, locale=None, limit=20, offset=0) #Get artist country

# Data we want from artist name (creates artist object)
- image (spotify API) (achievable)
- description (spotifyAPI) (maybe not avaliable)
- country (spotifyAPI) (achievable)
- genre(spotifyAPI) (achievable)
- toptracks(spotifyAPI) (achievable)
- festivalplayingat(ParentClassFestival)

Where to store artist object? semi permanently?
Daily api gets? or every user request?
What to do if data is not avaliable? (what if no spotify?) (what if no description?)
