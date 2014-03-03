A simple [last.fm](www.last.fm) crawler.

Recommends songs by artists who are (more or less) similar to your favorite artist.

###Installation
```
pip install scrapy
git clone git@github.com:ssbl/songhelper.git
```

##Examples

###Scraping
```
scrapy crawl songhelper -a artist='Pink Floyd'
```

###Output

To save the scraped data in a json file (here items.json), run the spider like this:
```
scrapy crawl songhelper -a artist='Pink Floyd' -o items.json -t json
```

The contents of the json file will look like:
```
{"album": "Led Zeppelin IV", "link": "http://www.last.fm/music/Led+Zeppelin/_/Stairway+to+Heaven", 
  "name": "Stairway to Heaven", "artist": "Led Zeppelin"},
  ...
```
