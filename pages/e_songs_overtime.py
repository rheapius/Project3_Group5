#e_Songs Overtime
import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
from sqlalchemy import create_engine
import plotly.graph_objects as go

dash.register_page(__name__, path='/songs_overtime', name="Songs Overtime")

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

####################### LAYOUT #############################
layout = html.Div(
    [
        html.H4("Timeline Attritube Analysis"),
        dcc.Graph(id="time-series-chart"),
        html.P("Select attribute:"),
        dcc.Dropdown(
            id="ticker",
            options=["BPM", "Dancebility", "Valence", "Energy", "Acousticness", "Instrumentalness", "Liveness", "Speechiness"],
            value="BPM",
            clearable=False,
        ),
    ]
)
####################### BUILD CHART #############################

@callback(
    Output("time-series-chart", "figure"), [Input("ticker", "value")]
)
def display_time_series(ticker):
   # datetime col
    df['Release_date'] = pd.to_datetime(df['Release_date'])
    # year 
    df['Release_year'] = df['Release_date'].dt.year
    # group by year
    yearly_avg = df.groupby('Release_year')[ticker].mean().reset_index()

    # group by year and streams 
    yearly_streams_total = df.groupby('Release_year')['Streams'].sum().reset_index()

    # fig object 
    fig = go.Figure()

    # add line on 2nd y axis 
    fig.add_trace(go.Scatter(x=yearly_avg['Release_year'], y=yearly_avg[ticker],
                             mode='lines+markers', name=f'Average {ticker}',
                             line=dict(color='blue')))
    # add trace 
    fig.add_trace(go.Scatter(x=yearly_streams_total['Release_year'], y=yearly_streams_total['Streams'],
                             mode='lines+markers', name='Total Streams',
                             line=dict(color='red'), yaxis='y2'))
    #update fig 
    fig.update_layout(
        title=f"Average {ticker} and Total Streams Over Time",
        xaxis_title='Release Year',
        yaxis=dict(title=f'Average {ticker}', showgrid=True, color='blue'),
        yaxis2=dict(title='Total Streams', overlaying='y', side='right', showgrid=False, color='red'),
        legend=dict(x=0.01, y=0.99, bordercolor='Black', borderwidth=1)
    )

    return fig

    