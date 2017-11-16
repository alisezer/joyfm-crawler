import pandas as pd
import os

project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           os.pardir)
data_dir = os.path.join(project_dir, 'data')
initial_csv_path = os.path.join(data_dir, 'songs.csv')
final_csv_path = os.path.join(data_dir, 'final_songs.csv')


def transform_csv():
    # Load CSV
    songs_csv = pd.read_csv(initial_csv_path)

    # Remove Errors
    songs_csv = songs_csv[songs_csv['song'] != 'ERROR']

    # Remove Duplicates
    songs_csv.drop_duplicates(subset=['song', 'artist'], keep='first',
                              inplace=True)

    # Save CSV
    songs_csv.reset_index(drop=True, inplace=True)
    songs_csv = songs_csv[['song', 'artist']]
    songs_csv.to_csv(final_csv_path, index=False, encoding='utf-8')


if __name__ == '__main__':
    transform_csv()
