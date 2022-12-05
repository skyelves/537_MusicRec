import os
from google.cloud import bigquery

def create_bqclient(access_key_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = access_key_path
    client = bigquery.Client().from_service_account_json(access_key_path)
    return client

def run_query(client, genre):
    query_job = client.query(
        f"""
        SELECT tracks.track_id, tracks.track_name, tracks.popularity, albums.album_id, albums.album_name, albums.total_tracks, albums.artist_id, artists.artist_name, artists.genre1
        FROM music_data.tracks left JOIN music_data.albums
        on tracks.album_id=albums.album_id
        left join music_data.artists
        on albums.artist_id=artists.artist_id
        where artists.genre1="{genre}"
        ORDER BY tracks.popularity DESC
        limit 10;
        """
        )
    df = query_job.to_dataframe()
    return df
