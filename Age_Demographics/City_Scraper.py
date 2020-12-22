# This script goes through all 50 state pages on city-data.com 
# and saves a list of every city and its city-data url

import requests, bs4, pickle

res = requests.get('https://www.city-data.com/')
soup = bs4.BeautifulSoup(res.text, 'html.parser')

links = soup.find_all('a')

state_links = []

# Quicker to filter list of all links than to type out every single state by hand
for link in links:
    try:
        if '/city/' in link['href']:
            state_links.append(link['href'])
    except:
        continue

# Scrape
city_links = []
for link in state_links:
    res = requests.get('https://city-data.com' + link)
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    state = link[6:-5]
    print(state)
    for a in soup.find_all('a'):
        if '-' + state + '.html' in a['href']:
            city_links.append(a['href'])
            
# Save data
with open('Data/links.pickle', 'wb') as pik:
    pickle.dump(city_links, pik)


