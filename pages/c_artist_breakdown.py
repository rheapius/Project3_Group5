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
    Input("dropdown", "value"),
)
# def change_artist(artist):
#     scatter_fig = px.scatter(
#             df[df["Artist"].isin([artist])], x='Dancebility', y='Streams', color='Dancebility',
#             title=f'Scatter Plot of Danceability vs. Number of Streams for artist_name',
#             labels={'Dancebility': 'Danceability', 'Streams': 'Number of Streams'},
#             hover_data={'Artist': True}, 
#     )
#     return scatter_fig

def change_artist(artist):
    fig_3d_scatter = px.scatter_3d(df[df["Artist"].isin([artist])], x='Dancebility', y='BPM', z='Speechiness', color='Streams',
                               size='Streams', hover_name='Track',
                               title='BPM vs. Speechiness vs. Danceability', color_continuous_scale= "Plasma", width= 1500, height= 800)
    return fig_3d_scatter


####################### PAGE LAYOUT #############################
layout = html.Div(
    [
        html.H4("Interactive Danceability vs Streams of Artists Songs"),
        html.P("Artist Selected:"),
        dcc.Dropdown(
            id="dropdown", options=options, value="Taylor Swift"
        ),
        dcc.Graph(id="scatter"),
    ]
)


