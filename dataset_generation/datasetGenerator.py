ACCESS_TOKEN = "Lv_zMqRlLAhho36VAGdZa9w1Q-N0BmB3v4TzYAwh8MGgK05O6yZmGpbV0Ewt1KLM"

import lyricsgenius
import pandas as pd

# Set up the Genius API client
genius = lyricsgenius.Genius(ACCESS_TOKEN)

# Search for songs of a particular genre
search_query = "genre:{genre_name}"
search_results = genius.search_songs(search_query, per_page=50)

# Extract the desired information for each track
tracks = []
for hit in search_results['hits'][:100]:
    lyrics = hit['result'].get('lyrics', None)
    release_date = hit['result'].get('release_date')
    if release_date is not None:
        release_year = release_date.split('-')[0]
    else:
        release_year = None
    track = {
        'artist_name': hit['result']['primary_artist']['name'],
        'track_name': hit['result']['title'],
        'release_date': release_year,
        'genre': 'Indie',
        'lyrics': lyrics
    }
    tracks.append(track)

# Create a pandas DataFrame from the tracks list
df = pd.DataFrame(tracks)

# Save the DataFrame to a CSV file
df.to_csv('Student_dataset.csv', index=False)
