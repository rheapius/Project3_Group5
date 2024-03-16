import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
from sqlalchemy import create_engine

dash.register_page(__name__, path='/top_ten_songs', name="Top Ten Songs")

####################### LOAD DATASET #############################
# Create a SQLAlchemy engine to connect to the SQLite database
engine = create_engine('sqlite:///topsongs.sqlite')

# Query to select data from the "tracks" table
query = "SELECT * FROM tracks"
query1 = "SELECT * FROM artists"
# Read data from the "tracks" table into a Pandas DataFrame
df = pd.read_sql_query(query, engine)
df1 = pd.read_sql_query(query1, engine)
engine.dispose()

####################### BAR CHART #############################
def get_top_songs(df, n=10):
#     Sorts the DataFrame by the number of Streams in descending order and selects the top N songs.    
#     Parameters:
#         df (DataFrame): The DataFrame containing the song data.
#         n (int): The number of top songs to select (default is 10).    
#     Returns:
#         DataFrame: The DataFrame containing the top N songs.   
    top_songs = df.sort_values(by='Streams', ascending=False).head(n)
    return top_songs

def create_bar_chart(top_songs):
#    Creates a bar chart for the top N songs with each song having a different color.    
#     Parameters:
#         top_songs (DataFrame): The DataFrame containing the top N songs.
   #Create bar chart
    fig_bar = px.bar(top_songs, x='Track', y='Streams',
                 title='Top Songs by Number of Streams', color='Track')
    return  fig_bar

####################### PIE CHART #############################

def create_pie_chart(top_songs):
#     Creates a pie chart of the top N songs based on their Key.
#     Parameters:
#         top_songs (DataFrame): The DataFrame containing the song data.
    # Count the number of occurrences of each 'Key' value
    key_counts = df['Key'].value_counts()

    # Create pie chart
    fig_pie = px.pie(top_songs, values=key_counts.values, names=key_counts.index, title='Top 10 Songs by Key')
    return fig_pie


top_songs = get_top_songs(df, n=10)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    dcc.Graph(figure = create_bar_chart(top_songs)),
    html.Br(),
    dcc.Graph(figure = create_pie_chart(top_songs))
])

####################### CALLBACKS ################################
