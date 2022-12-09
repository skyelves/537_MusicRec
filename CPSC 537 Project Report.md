# CPSC 537 Project Report

## Team Member

Ke Wang	            kw754

Weiyi Li                 wl468

Ji Yoon Lee	        jl3699

Weiqiang Zheng  wz347

## Introduction and project goals

With the growing popularity of streaming music platforms such as Pandora, Spotify, Apple music, automatic playlist continuation (APC) has drawn increasing attention in recent years. Music recommendation is a process in which a computer algorithm suggests songs or other pieces of music to a user based on their personal preferences and listening history. This technology has become increasingly important in recent years as more and more people use streaming services to listen to music. By providing personalized recommendations, these services can help users discover new music that they might enjoy, as well as help them find their favorite songs and artists more easily.

In this project, we will use collected online data through Spotify API and AIcrowd competitions to provide musical recommendations for users. We simplify the task by direct ask users to submit their keywords and our application will return a list of songs based on their preferences. The project goals are following: 

1. We collect and clean the data using Python (e.g. package pandas, requests) .
2. We store the data in BigQuery on Google Cloud Platform. The data is well-organized in several tables. 
3. We implement our strategy of recommendation using SQL. 
4. We also build an user-friendly interface for the application. 

## Description of Data

1. The first dataset we utilize is collected through [Spotify API][1]. We retrieve information about artists, albums, and tracks, as well as data about a user's listening history and preferences.

2. The second dataset is the [*Spotify Million Playlist Dataset Challenge*][2], which is a dataset and open-ended challenge for music recommendation research. 

   [1]: https://developer.spotify.com/documentation/web-api/	"Spotify API"
   [2]: https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge	"Spotify Million Playlist Dataset Challenge"

## Basic architecture

1. Data collection: This part is responsible for collecting data about the songs and artists.  We collected data from Spotify API and an online recommendation challenge dataset. The details of the data that we gathered is given above in the "Description of Data" section. 

2. Data processing: This part is responsible for cleaning and preprocessing the data collected from various sources, and organizing it into a form that can be used by the recommendation function. We cleaned the data using Python and then stored the data in BigQuery on Google Could Forms. The data is organized in four tables: album, artists, playlist, and tracks. 

3. Recommendation function: Implementing a sophisticated recommendation algorithm is beyond the scope of this project, as the main goal is to use the database system in a pratical application. Thus we implemented two simply recommendation strategis: (1) If the user submits a name of artist, we will return a list of songs by this artist and similar artists. (2) If the user submits a genre of music, we will return a list of songs related genres. The two strategies, are simple by requires *complex* SQL queries with multiple joins, subqueries, and aggregation. 

4. User interface: This part is responsible for presenting the recommendations to users and allowing them to interact with the system. We used [Flask][3] to bulid the user interface. User may submit "Artist", "Genre", "Number" and get a list of recommended songs with the specified number. 

   [3]: https://flask.palletsprojects.com/en/2.2.x/	"Flask"

## Key features of the project and Technical Challenges

1. We implemented a simple yet beautifull user interface on web using Flask. This enables users to easily interact with the system. This is a technical challenge for us since we have to learn how to use Flask. Below are two screenshots of our user interface. ![截屏2022-12-08 下午6.06.28](/Users/weiqiangsmac/Dropbox/Mac (2)/Desktop/截屏2022-12-08 下午6.06.28.png)![截屏2022-12-08 下午6.14.08](/Users/weiqiangsmac/Dropbox/Mac (2)/Desktop/截屏2022-12-08 下午6.14.08.png)

2. In the implementation of our recommendation function, we included two complex SQL queries, each with multiple joins and aggregation. 

   ```sql
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
   ```

   ```sql
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
   ```