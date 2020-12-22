from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import pickle

import re, time, sys
tm = time.time()
coordPattern = re.compile(r'@(-?\d+\.\d+),(-?\d+\.\d+)')


with open('../Data/ages.pickle', 'rb') as pik:
    dicto = pickle.load(pik)

places = list(dicto.keys()) 
def getCoords(url):
    lat = float(coordPattern.search(url).group(1))
    lng = float(coordPattern.search(url).group(2))
    return lat, lng


driver = webdriver.Firefox()

timeout = False
df = {'Place': [], 'Lat': [], 'Lng': [], 'Median Age': []}
for place in places:
    #Go to maps
    driver.get(f'https://Google.com/maps/search/{place}')
    time.sleep(1)

    while driver.current_url == 'https://www.google.com/maps':
        continue
    check = time.time()
    while 'search' in driver.current_url:
        timeElapsed = time.time() - check
        if timeElapsed > 5:
            timeout = True
            print(f'Google couldn\'t find any results for {place}. Try being more specific.')
            break
        continue

    if timeout:
        timeout = False
        continue

    url = driver.current_url
    try:
        lat, lng = getCoords(url)
    except:
        print(f'Error at {place}')
        print(f'URL: {url}')
        continue
    df['Place'].append(place)
    df['Lat'].append(lat)
    df['Lng'].append(lng)
    df['Median Age'].append(dicto[place])
    print(f'{place}: ({lat}, {lng})')

df = pd.DataFrame(df)

filename = '../Data/places.csv' 
df.to_csv(filename)

driver.quit()
complete = (time.time() - tm) / 60

print(f'It took you {complete} minutes to scrape {len(places)} places!')
