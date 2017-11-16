import pandas as pd


def transform_csv():
    # Load CSV
    songs_csv = pd.read_csv('songs.csv')

    # Remove Errors
    songs_csv = songs_csv[songs_csv['song'] != 'ERROR']

    # Remove Duplicates
    songs_csv.drop_duplicates(subset=['song', 'artist'], keep='first',
                              inplace=True)

    # Save CSV
    songs_csv.reset_index(drop=True, inplace=True)
    songs_csv = songs_csv[['song', 'artist']]
    songs_csv.to_csv('final_songs.csv', index=False, encoding='utf-8')


if __name__ == '__main__':
    transform_csv()