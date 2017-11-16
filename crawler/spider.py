from bs4 import BeautifulSoup
import requests as rq
import os
import pandas as pd
import logging
import datetime
import time

TARGET_URL = 'https://karnaval.com/radyolar/joyfm'

# Logger Setup
logger = logging.getLogger(__name__)


class JoySpider(object):

    def __init__(self):
        """Initial class generation - mostly sets right directories"""

        self.target_url = TARGET_URL
        self.project_dir = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), os.pardir)
        self.data_dir = os.path.join(self.project_dir, 'data')
        self.csv_path = os.path.join(self.data_dir, 'songs.csv')

    def get_song_information(self, verbose=False):
        """Gets the current playing song from joy FM

        Args:
            verbose: If true, prints the song and current artist

        Returns:
            Song name and artist name
        """

        # Make request to Joy FM
        response = rq.get(self.target_url)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')
        # Find where the title is
        container = soup.find(
            'div', class_='station_now_playing_container station_3')

        # Save song name and artist
        song_name = str(container.find('span', class_='title').text)
        artist = str(container.find('span', class_='sub_title').text)

        if verbose:
            display_text = 'Current Song: {0} -- Current Artist: {1}'.\
                format(song_name, artist)
            logger.info(display_text)
        return song_name, artist

    def display_current_song(self):
        """Display current song without saving"""

        self.get_song_information(verbose=True)

    def create_csv(self):
        """Creates songs.csv in the data folder"""

        songs_df = pd.DataFrame(columns=[['song', 'artist', 'time']])
        songs_df.to_csv(self.csv_path, index=False, encoding='utf-8')
        logger.info('CSV Created: {}'.format(self.csv_path))

    def save_df(self, df):
        """Saves a df in the csv format"""

        df.to_csv(self.csv_path, index=False, encoding='utf-8')
        logger.debug('CSV Saved: {}'.format(self.csv_path))

    def retrieve_df(self):
        """Retrieves song csv

        Returns:
            Pandas df
        """

        retrieved_df = pd.read_csv(self.csv_path)
        logger.debug('CSV Retrieved: {}'.format(self.csv_path))
        return retrieved_df

    def check_csv_exists(self):
        """Checks if CSV exists

        Returns:
            True if yes, False if not
        """

        return os.path.isfile(self.csv_path)

    def single_run(self):
        """" Runs the pipeline once, saves the song to csv
        Notes:
            Saves results to songs.csv
        """
        if not self.check_csv_exists():
            self.create_csv()

        songs_df = self.retrieve_df()

        current_time = datetime.datetime.utcnow()

        try:
            current_song, current_artist = self.get_song_information(True)
        except Exception as e:
            logger.error('Something Went Wrong')
            logger.error(e)
            current_song = 'ERROR'
            current_artist = 'ERROR'
        data = [current_song, current_artist, current_time]
        temp_df = pd.DataFrame(data=[data],
                               columns=['song', 'artist', 'time'])
        songs_df = songs_df.append(temp_df)
        songs_df.reset_index(inplace=True, drop=True)
        self.save_df(songs_df)
        logger.info('Song information saved')

    def counted_run(self, count=5):
        """Runs the pipeline as many times as stated in the count, with 60
        sec intervals

        Args:
            count: Number of times to run the pipeline
        Notes:
            Saves results to songs.csv
        """
        logger.info('Beginning counted run for {} times'.format(count))
        i = 0
        while True:
            self.single_run()
            i += 1
            if i == count:
                break
            time.sleep(60)
        logger.info('Counted run complete')

    def timed_run(self, days=0, hours=1):
        """Runs the pipeline for given days and hours

        Args:
            days: How many days should it keep going for?
            hours: How many hours should it keep going for?
        Notes:
            Saves results to songs.csv
        """
        logger.info('Beginning timed run for {} days and {} hours'.
                    format(days, hours))

        minutes = days*3600 + hours*60
        i = 0
        while True:
            self.single_run()
            i += 1
            if i == minutes:
                break
            time.sleep(59)
        logger.info('Timed run complete')
