# JOY FM CRAWLER

## INTRO
Joy FM is a radio station and has an online website where you can listen to. 
They feature songs ideal for working or relaxing. This little project aims to create
a small web spider to create a playlist based on the songs they play. The spider 
objective will be to ping their website every minute, and save the song data present 
at that minute.

## ENV SETUP
```shell
virtualenv -p python2 venv
source venv/bin/activate
pip install -r requirements
```

## SPIDER CONFIGURATION

### Single Run
For a single run (get me which song is playing now):

```python
from crawler.spider import JoySpider
my_spider = JoySpider()
my_spider.single_run()
```

### Counted Run
Get me which song is playing for x many times(Lets say x is 382):
```python
from crawler.spider import JoySpider
my_spider = JoySpider()
my_spider.counted_run(count=382)
```

### Time Run
Get me which song is playing for until a specified time(Lets say 5 Days and 2 Hours):
```python
from crawler.spider import JoySpider
my_spider = JoySpider()
my_spider.timed_run(days=5, hours=0)
```


In all runs, a CSV will be generated and saved under the data folder

## DATA TRANSFORMATION  

The initial CSV will have ERROR and duplicate columns. In order to get rid of them and generate a final CSV:

```shell
python -m data.transformation 
```

Which will give you the final CSV!


## FINAL

If you would like to convert this CSV to a Spotify Playlist of yours:
http://www.playlist-converter.net/



Enjoy!
