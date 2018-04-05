# tweets-around-me

A DBless Django 2.0 example to search for tweets around given coordinates using Twython.

## Usage
1. The index page asks you for latitude and longitude, they both have an html form check on format type (float), min and max. 
2. Once you provide them, you'll see an embedded map centered on the given coordinates and a marker for every geo tweet, if any available. 
3. Clicking on the marker you will access the tweet in Twitter. 

## About geo tweets
* Do not expect a lot of geo tweets, they are not that common.
* The count for every search is set to 100, the maximum. Then geo tweets are filtered.
* Search radius is 50km.
