# This script takes a list of city-data.com URLs and creates a dictionary
# where the keys are cities, and the values are median ages
# These cities will be scraped using Google Places API and visualized with gmaps
import requests, pickle, bs4, os


#Proxy server
proxies = {
        'https': '163.153.214.50:8080' 
}


# From City_Scraper
with open('Data/links.pickle', 'rb') as pik:
    links = pickle.load(pik)


ageDict = {}

#Check if there is already age info present (ie, you started the program and the internet went out halfway through)
if 'ages.pickle' in os.listdir('Data'):
    with open('Data/ages.pickle', 'rb') as pik:
        ageDict = pickle.load(pik)
		
# Scrape
for link in links:
    try:
        url = 'https://www.city-data.com/city/' + link
        name = link[:-5]
        if '/' in name:
            continue
        if name in ageDict.keys():
            continue
     
        res = requests.get(url)#,proxies=proxies)
        
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        tag = soup.find('section', attrs={'class':'median-age'})
        median_age = float(tag.text[20:24])
        ageDict[name] = median_age
        print(name)
	
	#Save dictionary to pickle file at every iteration 
	#in case of internet problems and lost work
        with open('Data/ages.pickle', 'wb') as pik:
            pickle.dump(ageDict, pik)
    except Exception as e:
        print('########################################################################################\nERROR########################################################################################')
        print(str(e))
        continue
