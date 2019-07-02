import requests #Import Requests Library
result = requests.get("https://www.roskilde-festival.dk/en/line-up/") #Select page to scrape

#print(result.status_code) #Make sure we got a result (should return 200)
#print(result.headers) #Return header info
#print(result.content) #Returrns all results from page

import requests #Import Requests Library
result = requests.get("https://www.roskilde-festival.dk/en/line-up/") #Select page to scrape

# Store content in accesible variable
c = result.content

# Start parsing data with Beautifoulsoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(c, 'html.parser')
samples = soup.find_all("a", "name")

# Prints all elements in stripped list
for artist in samples:
    for string in artist.stripped_strings:
        print(repr(string))
