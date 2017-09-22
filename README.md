# Joy FM Playlist Crawler

Without a doubt Joy FM is one of the best radio stations in Turkey. The goal of 
this project is to ping their website every so often, gather the current song 
and artist information, and save it!

### Installation

After cloning the repository from Github and opening the directory in your terminal:
```sh
virtualenv venv
source venv/bin/activate
pip install -e .

```

### Running the package

####Single Mode:
Runs the program once and saves data to songs.csv under the data folder

```sh
joycrawler single
```

####Counted Mode:
Runs the program multiple times (stated with the count variable) with 60 second 
intervals and saves data to songs.csv under the data folder
```sh
joycrawler counted --count 10
```

####Timed Mode:
Runs the program for a given time (stated with days and hours variables) with 
60 second intervals and saves data to songs.csv under the data folder
```sh
joycrawler timed --days 10 --hours 5
```

_This will run the pipeline for 10 days and 5 hours_

###Data
Data will be saved in a CSV under the data folder. 