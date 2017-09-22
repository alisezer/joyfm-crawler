from bs4 import BeautifulSoup
import requests as rq
import os
import pandas as pd
import logging
import datetime
import time

TARGET_URL = 'https://karnaval.com/radyolar/joyfm'


# Logger config
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
level = 'INFO'
logging.basicConfig(level=level, format=log_fmt)

# Logger Setup
logger = logging.getLogger(__name__)


class JoySpider(object):

    def __init__(self):
        self.target_url = TARGET_URL
        self.project_dir = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), os.pardir)
        self.data_dir = os.path.join(self.project_dir, 'data')
        self.csv_path = os.path.join(self.data_dir, 'songs.csv')

    def get_song_information(self, verbose=False):
        response = rq.get(self.target_url)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')
        container = soup.find('div',
                              class_='station_now_playing_container station_3')

        song_name = str(container.find('span', class_='title').text)
        artist = str(container.find('span', class_='sub_title').text)

        if verbose:
            display_text = 'Current Song: {0} -- Current Artist: {1}'.\
                format(song_name, artist)
            logger.info(display_text)
        return song_name, artist

    def display_current_song(self):
        self.get_song_information(verbose=True)

    def create_csv(self):
        songs_df = pd.DataFrame(columns=[['song', 'artist', 'time']])
        songs_df.to_csv(self.csv_path, index=False, encoding='utf-8')
        logger.info('CSV Created: {}'.format(self.csv_path))

    def save_df(self, df):
        df.to_csv(self.csv_path, index=False, encoding='utf-8')
        logger.debug('CSV Saved: {}'.format(self.csv_path))

    def retrieve_df(self):
        retrieved_df = pd.read_csv(self.csv_path)
        logger.debug('CSV Retrieved: {}'.format(self.csv_path))
        return retrieved_df

    def check_csv_exists(self):
        return os.path.isfile(self.csv_path)

    def single_run(self):
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
        logger.info('Beginning timed run for {} days and {} hours'.
                    format(days, hours))

        minutes = days*3600 + hours*60
        i =0
        while True:
            self.single_run()
            i += 1
            if i == minutes:
                break
            time.sleep(59)
        logger.info('Timed run complete')


if __name__ == '__main__':
    JoySpider().counted_run(10)
