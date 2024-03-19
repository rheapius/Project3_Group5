# Most Streamed Songs & Artists

## Overview:
Visualize top 10 songs & artists based on streaming. Song attributes are analysed & visualized.

Dashboard link: https://music-analysis-app.onrender.com/

## Aim
The aim of our project is to uncover patterns in Spotify’s playlist for 2023. We’ll examine what makes a song popular and whether song characteristics have changed over time.
Characteristics examined include the beats per minute, the main key of the music and whether a particular artist features more prominently in the charts.

## Data cleaning 
The data was obtained as a CSV file and then cleaned up using Jupyter notebook. The NAN values were removed, columns renamed and string values were converted to numeric values. The 'Data_cleaning' folder houses the csv files with cleaned data.
The Jupyter notebook ('datacleaning.ipynb') used to clean the data has also been saved in this folder.

## Database loading
SQlite database has been used to store the data for tracks, artists, and separate classes for each music streaming service (Spotify, Apple, Deezer & Shazam). 
The Jupyter notebook ('database.ipynb') used to create this database has been saved in the 'Data_cleaning' folder.
The database file ('topsongs.sqlite') is saved in the main repository.

## Data Visualisation
Using Jupyter Notebook to test the plots to be created. Using plotly.express as the modelling tool
https://plotly.com/python/line-and-scatter/#scatter-plots-in-dash - referenced for creation of bubble chart.
Using functions to call the various plots as required by the html pages.

## Instructions for Web Page
The webpage has interactive tabs for welcome page, dataset, top ten songs, artist breakdown, attribute summary/correlation & songs overtime.
The artist breakdown tab lets users select artists and their song attributes for visualisation.
Attribute summary tab allows users to select a song attribute to show its distribution in top 100 songs.
Songs overtime tab visualises changes in a chosen attribute with total streamed songs over a period of time.

Website link - https://music-analysis-app.onrender.com/

## Ethical considerations
The dataset gives us the stream count of each song and other information regarding the songs. The stream count data is collected by Spotify, a music streaming service. Spotify users agree to this data collection when they sign up for a new account. This has been mentioned in their privacy policy.


## References & Datasets

Most Streamed Spotify Songs 2023- Kaggle Dataset https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/data

Spotify privacy policy https://www.spotify.com/au/legal/privacy-policy/

Plotly.express https://plotly.com/python

Understanding music keys: https://www.pianote.com/blog/c-db-scales/ 




