#streamed_song_summary

import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
from sqlalchemy import create_engine


dash.register_page(__name__, path='/streamed_song_summary', name="Streamed Song Summary")

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

####################### CHART BUILDER #############################

def create_bubble_chart(df):
    bubble = px.scatter(df, x="Track", y="Streams", color="Artist",
                 size='Streams', hover_data=['Track'])
    bubble.update_layout(height=1000, width=1500)
    return bubble

####################### PAGE LAYOUT #############################
layout = html.Div(
    [
        html.H4("Streamed Songs Summary"),
        html.P("Song attribute selected:"),
        dcc.RadioItems(
            id="selection", options = ["BPM", "Key", "Mode", "Dancebility", "Valence", "Energy", "Acousticness", "Instrumentalness", "Liveness", "Speechiness"], value="BPM"
        ),
        dcc.Graph(id="histogram"),
        html.H4("Bubble Chart of All Songs"),
        dcc.Graph(figure = create_bubble_chart(df))
    ]
)

####################### CALLBACKS ################################
@callback(
    Output("histogram", "figure"),
    Input("selection", "value"),
)
def change_artist(col = "BPM"):
    histogram = px.histogram(df, x= col, title='Distribution of Beats per minute (bpm)')
    return histogram


