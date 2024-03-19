import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
from sqlalchemy import create_engine

dash.register_page(__name__, path='/artist_breakdown', name="Artist Breakdown")

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

####################### SCATTER PLOT #############################

# Filter df1 for rows where the 'Artist' column contains the user input (partial match)
artist_data = df["Artist"].unique().tolist()
options = [{"label": artist.capitalize(), "value": artist} for artist in artist_data]

####################### CALLBACKS ################################
@callback(
    Output("scatter", "figure"),
    [Input("dropdown", "value"),
    Input("x-axis-dropdown", "value"),
    Input("y-axis-dropdown", "value"),
    Input("z-axis-dropdown", "value"),
    Input("colour-by-dropdown", "value")]
)

def change_artist(artist, x_a = "Dancebility", y_a = "BPM", z_a = "Speechiness", colour_by="Streams"):
    color_scale = "Plasma" if colour_by == "Streams" else None

    fig_3d_scatter = px.scatter_3d(df[df["Artist"].isin(artist)], x= x_a, y= y_a, z= z_a, color=colour_by,
                               size='Streams', hover_name= 'Track', hover_data = ['Artist'],
                               title=f'{x_a} vs. {y_a} vs. {z_a}', color_continuous_scale= color_scale, width= 1000, height= 600)
    return fig_3d_scatter

####################### PAGE LAYOUT #############################
layout = html.Div([
    html.H4("Interactive Attribute Breakdown of Artist(s) Songs", style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            html.P("Artist(s) Selected:"),
            dcc.Dropdown(
                id="dropdown",
                options=options,
                value=["Taylor Swift"],
                multi= True
            )
        ], style={'flex': '1', 'marginRight': '20px'}),  

        html.Div([
            html.P("X Axis Attribute:"),
            dcc.Dropdown(
                id="x-axis-dropdown",
                options=["BPM", "Key", "Mode", "Dancebility", "Valence", "Energy", "Acousticness", "Instrumentalness", "Liveness", "Speechiness"],
                value="Dancebility"
            )
        ], style={'flex': '1', 'marginRight': '20px'}),

        html.Div([
            html.P("Y Axis Attribute:"),
            dcc.Dropdown(
                id="y-axis-dropdown",
                options=["BPM", "Key", "Mode", "Dancebility", "Valence", "Energy", "Acousticness", "Instrumentalness", "Liveness", "Speechiness"],
                value="BPM"
            )
        ], style={'flex': '1', 'marginRight': '20px'}),

        html.Div([
            html.P("Z Axis Attribute:"),
            dcc.Dropdown(
                id="z-axis-dropdown",
                options=["BPM", "Key", "Mode", "Dancebility", "Valence", "Energy", "Acousticness", "Instrumentalness", "Liveness", "Speechiness"],
                value="Speechiness"
            )
        ], style={'flex': '1'}),

        html.Div([
            html.P("Colour By:"),
            dcc.Dropdown(
                id="colour-by-dropdown",
                options=[
                    {"label": "Streams", "value": "Streams"},
                    {"label": "Artist", "value": "Artist"}
                ],
                value="Streams" 
            )
        ], style={'flex': '1', 'marginRight': '20px', 'marginTop': '20px'}),

    ], style={'display': 'flex', 'flexWrap': 'wrap', 'alignItems': 'flex-end', 'justifyContent': 'center'}),
    
    dcc.Graph(id="scatter"),

    html.Div(children=[
        html.Br(),
        html.H5("Song Attribute Descriptions"),
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
    ]),
], style={'padding': '20px'})



