from bs4 import BeautifulSoup
import requests as rq


TARGET_URL = 'https://karnaval.com/radyolar/joyfm'


def get_song_information(verbose=False):
    response = rq.get(TARGET_URL)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    container = soup.find('div',
                          class_='station_now_playing_container station_3')

    song_name = container.find('span', class_='title').text
    artist = container.find('span', class_='sub_title').text

    if verbose:
        print "Current Song  :", song_name
        print "Current Artist:", artist
    return song_name, artist


if __name__ == '__main__':
    get_song_information(verbose=True)
