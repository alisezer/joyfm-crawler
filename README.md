# JOY FM CRAWLER

## Intro
Without a doubt Joy FM is one of the best radio stations in Turkey. This little 
project creates a small web spider to compose a playlist from the songs they play. 
The spider can ping their website, and saves the song data present at that minute.

## Installation

After cloning the repository from Github and opening the directory in your terminal:
```sh
virtualenv venv
source venv/bin/activate
pip install -p python2.7 -e .

```

## Running the package

### Single Mode:
Runs the program once and saves data to songs.csv under the data folder

```sh
joycrawler single
```

### Counted Mode:
Runs the program multiple times (stated with the count variable) with 60 second 
intervals and saves data to songs.csv under the data folder
```sh
joycrawler counted --count 10
```

### Timed Mode:
Runs the program for a given time (stated with days and hours variables) with 
60 second intervals and saves data to songs.csv under the data folder
```sh
joycrawler timed --days 10 --hours 5
```

_This will run the pipeline for 10 days and 5 hours_

### Data
Data will be saved in a CSV under the data folder. 


In all runs, a CSV will be generated and saved under the data folder

## Data Transformation 

The initial CSV will have ERROR and duplicate columns. In order to get rid of them and generate a final CSV:

```shell
joycrawler transform_data
```

Which will give you the final CSV!


## Final

If you would like to convert this CSV to a Spotify Playlist of yours:
http://www.playlist-converter.net/

The Playlist I created: 
https://open.spotify.com/user/malisezer/playlist/2ZlhTr6AOgh5pZLZYyEcBy

Enjoy!
