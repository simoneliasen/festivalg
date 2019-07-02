#Webscraper for Roskilde Festival
import requests #Import Requests Library
result = requests.get("https://www.roskilde-festival.dk/en/line-up/") #Select page to scrape

#print(result.status_code) #Make sure we got a result (should return 200)
#print(result.headers) #Return header info
#print(result.content) #Returrns all results from page

# Store content in accesible variable
c = result.content

# Start parsing data with Beautifoulsoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(c, 'xml')
samples = soup.find_all("a", "name")

# Prints all artists in list (removes white space)
for artist in samples:
    print(list(artist.stripped_strings)[0])

# Check for lenght throw error if empty?? made by echo (i don't get this)
x = list(artist.stripped_strings)
if x:
    print(x[0])
