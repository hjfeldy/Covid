# Geographical / Age Web Scraper
This tool scrapes age demographic data from city-data.com and geographical data from Google Maps. Its purpose is to visualize the population distribution of the USA, weighted by median age. Each datapoint represents a city with a minimum population of 6000. To avoid the huge financial cost of making calls to the Google Places API, I scraped geographical data using the Selenium Webdriver.

## Instructions to replicate data collection on your own machine
1. Make sure you have beautiful soup installed (pip or conda will work)
2. Run City_Scraper.py (to get the list of 6000 cities)
3. Run Age_Scraper.py  (to make web requests to the 6000 cities)
4. Navigate to the Gmaps_Scraping folder and follow the directions inside
5. Input your Google api key into config.py to use the gmaps module
6. Run the Jupyter notebook inside the Map folder

Note: During your scraping city-data.com will most likely block your ip, but only for a little while. Without a VPN, you will have to run the script in sections. You will scrape about 10% of the website each time, and then get blocked. The script will save your progress, and the next time you run it, it will begin where you left off. They tend to let you back in within a few hours (but sometimes it takes longer). I highly suggest the use of a VPN for this script.
