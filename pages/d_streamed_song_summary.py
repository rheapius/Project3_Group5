#streamed_song_summary

import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
from sqlalchemy import create_engine

dash.register_page(__name__, path='/streamed_song_summary', name="Attribute Summary and Correlation")

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
# Define mapping of musical keys to numbers
key_to_number = {
    'A': 0,
    'A#': 1,
    'B': 2,
    'C#': 3,
    'D' : 4,
    'D#': 5,
    'E': 6,
    'F': 7,
    'F#': 8,
    'G': 9,
    'G#': 10
    }
    # Convert 'Keys' column from string to int using map function with default value -1
df2 = df
df2['Key'] = df2['Key'].str.upper().map(lambda x: key_to_number.get(x, -1))

# Select specific columns
selected_columns = ['BPM', 'Key','Dancebility', 'Valence', 'Energy', 'Acousticness', 'Instrumentalness', 'Liveness', 'Speechiness']
df_selected = df2[selected_columns]

# Compute correlation matrix
corr_matrix = df_selected.corr()
fig = px.imshow(corr_matrix,
                    labels=dict(x="Variables", y="Variables", color="Correlation"),
                    x=corr_matrix.index,
                    y=corr_matrix.columns,
                    color_continuous_scale='YlGnBu', title= 'Song Attribute Correlation Matrix')


def create_bubble_chart(df):
    bubble = px.scatter(df, x="Track", y="Streams", color="Artist",
                 size='Streams', hover_data=['Track'])
    bubble.update_layout(height=1000, width=1500)
    return bubble

####################### PAGE LAYOUT #############################
layout = html.Div([
    html.H4("Interactive Histogram Comparing Top 100 Songs Attributes to the Whole Dataset", style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            html.Br(),
            html.Br(),
            html.P("Song Attribute Selected:"),
            dcc.RadioItems(
                id="selection",
                options=["BPM", "Key", "Mode", "Dancebility", "Valence", "Energy", "Acousticness", "Instrumentalness", "Liveness", "Speechiness"],
                value="BPM"
            ),
        ], style={'width': '15%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        
        html.Div([
            dcc.Dropdown(
                id="track-selection",
                options=[
                    {"label": "Top 100 Tracks", "value": "top_100"},
                    {"label": "All Tracks", "value": "all"}
                ],
                value="all",  
                clearable=False
               
            ),
        ], style={'width': '15%', 'display': 'inline-block', 'verticalAlign': 'top'}),

        html.Div([
            dcc.Graph(id="histogram")
        ], style={'width': '70%', 'display': 'inline-block'}),
    ], style={'display': 'flex', 'justifyContent': 'center'}),
    
    html.Div([
        html.Div([
            html.Br(),
            html.P("Song Attribute Descriptions"),
            html.B("BPM: "), "Beats per minute, a measure of song tempo",
            html.Br(),
            html.B("Key: "), "Key of the song",
            html.Br(),
            html.B("Mode: "), "Mode of the song (major or minor)",
            html.Br(),
            html.B("Danceability: "), "Percentage indicating how suitable the song is for dancing",
            html.Br(),
            html.B("Valence: "), "Positivity of the song's musical content",
            html.Br(),
            html.B("Energy: "), "Perceived energy level of the song",
            html.Br(),
            html.B("Acousticness: "), "Amount of acoustic sound in the song",
            html.Br(),
            html.B("Instrumentalness: "), "Amount of instrumental content in the song",
            html.Br(),
            html.B("Liveness: "), "Presence of live performance elements",
            html.Br(),
            html.B("Speechiness: "), "Amount of spoken words in the song",
        ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'}),

        html.Div([
            dcc.Graph(figure=fig),
        ], style={'width': '70%', 'display': 'inline-block'}),
    ], style={'display': 'flex', 'justifyContent': 'center'}),

    html.H4("Bubble Chart of All Songs", style={'textAlign': 'center'}),
    dcc.Graph(figure=create_bubble_chart(df)),  
], style={'padding': '20px'})


####################### CALLBACKS ################################
@callback(
    Output("histogram", "figure"),
    [Input("selection", "value"),
     Input("track-selection", "value")] 
)

def update_histogram(col, track_selection):
    filtered_df = df  
   
    if track_selection == "top_100":
        filtered_df = df.nlargest(100, 'Streams')

    histogram = px.histogram(filtered_df, x=col, title=f'Distribution of {col}')
    return histogram