import os
from google.cloud import bigquery

def create_bqclient(access_key_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = access_key_path
    client = bigquery.Client().from_service_account_json(access_key_path)
    return client


def run_query(client, artist, genre, number):
    if not number:
        number = "10"
    if not artist:
        artist = "%"
    query = f"""
            SELECT tracks.track_name
            FROM music_data.tracks
            LEFT JOIN music_data.albums
            ON tracks.album_id = albums.album_id
            LEFT JOIN music_data.artists 
            ON albums.artist_id = artists.artist_id
            WHERE artists.artist_name = '{artist}'
            AND (artists.genre1 LIKE '%{genre}%' OR artists.genre2 LIKE '%{genre}%')
            ORDER BY tracks.popularity DESC
            LIMIT {number}
            """    
    query_job = client.query(query)
    iterator = query_job.result() 
    if iterator.total_rows > 0:
        res = [item[0] for item in iterator]
        return res

    query = f"""
            SELECT tracks.track_name
            FROM music_data.tracks
            LEFT JOIN music_data.albums
            ON tracks.album_id = albums.album_id
            LEFT JOIN music_data.artists 
            ON albums.artist_id = artists.artist_id
            WHERE artists.artist_name = '{artist}'
            OR artists.genre1 LIKE '%{genre}%' 
            OR artists.genre2 LIKE '%{genre}%'
            ORDER BY tracks.popularity DESC
            LIMIT {number}
            """   
    query_job = client.query(query)
    iterator = query_job.result() 
    res = [item[0] for item in iterator]
    return res
