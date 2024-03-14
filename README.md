# Most Streamed Songs & Artists

## Overview:
Visualize top 10 songs & artists based on streaming. 
Song aspects visualized using deployed Github pages

## Aim
The aim of our project is to uncover patterns in Spotify’s playlist for 2023. We’ll examine what makes a song popular and whether the songs are similarly popular on other streaming platforms.
To do this we will examine the beats per minute, the main key of the music and whether a particular artist features more prominently in the charts.

## Data cleaning 
The data was obtained as a CSV file and then cleaned up using Jupyter notebook. The NAN values were removed, columns renamed and string values were converted to numeric values. The 'Data_cleaning' folder houses the csv files with cleaned data.
The Jupyter notebook ('datacleaning.ipynb') used to clean the data has also been saved in this folder.

## Database loading
SQlite database has been used to store the data for tracks, artists, and separate classes for each music streaming service (Spotify, Apple, Deezer & Shazam). 
The Jupyter notebook ('database.ipynb') used to create this database has been saved in the 'Data_cleaning' folder.
The database file ('topsongs.sqlite') is saved in the main repository.

## Data Visualisation
Using Jupyter Notebook to test the plots to be created. Using plotly.express as the modelling tool
https://plotly.com/python/line-and-scatter/#scatter-plots-in-dash - referened for creation of bubble chart.
Using functions to call the various plots as required by the html pages.

## HTML page

## Ethical considerations
The dataset gives us the stream count of each song and other information regarding the songs. The stream count data is collected by Spotify, a music streaming service. Spotify users agree to this data collection when they sign up for a new account. This has been mentioned in their privacy policy.


## References & Datasets

Most Streamed Spotify Songs 2023- Kaggle Dataset https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/data

Spotify privacy policy https://www.spotify.com/au/legal/privacy-policy/

Plotly.express https://plotly.com/python




