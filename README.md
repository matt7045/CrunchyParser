# CrunchyParser
Goes out to Crunchyroll, and fetches the short descriptions for an anime of your choosing. 

## Required Programs and Libraries
* python   - Created with python 3.9, but other versions of python 3 may work. 
* firefox  - [Download Link Here](https://www.mozilla.org/firefox/download/thanks/)
* selenium - `pip install selenium`

## Use
* `getShortDescriptions(anime)`  - Returns a list of short descriptions of the passed `anime`. The parameter `anime` should match the name of the respective anime as it appears on crunchyroll. 
python```
from CrunchyParser import CrunchyParser   #Will start a selenium browser. Don't be spook'd

#Define some Anime
some_anime         = "hunter x hunter"
#Get the episode descriptions for that anime
anime_descriptions = CruncyParser.getShortDescriptions(some_anime) 
#Close the browser so it doesn't take up system resources
CrunchyParser.cleanup()     
```

Ez, breezy, covergirl. 

