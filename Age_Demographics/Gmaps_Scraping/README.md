# Google Maps Geo-Scraper
This script takes the age data we scraped from city-data.com and adds geographical information scraped from Google Maps urls. 

## Dependencies

In order for this script to work, you will need:
* Firefox
* Selenium (install with pip or conda)
* The proper [Geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.28.0) package for your OS (everything is supported)
* Geckodriver must be added to your PATH. I found [this](https://www.youtube.com/watch?v=iTyK5KGNx-Y) video to be helpful. 

## Instructions:

* Make sure to have run Age\_Scraper.py and City\_scraper.py (in that order)
* Configure dependencies
* Run main.py
* Enjoy free geographical information with no API. Now we can make a heatmap, which costs *far* less than calling the Google Places API 6000 times.

