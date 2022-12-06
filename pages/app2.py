#import necessary lib
import dash
from dash import html, dcc, Input, Output, callback   # pip install dash
import dash_bootstrap_components as dbc                # pip install dash_bootstrap_components
import pandas as pd
import plotly.express as px
import datetime
from datetime import datetime as dt

from .side_bar import sidebar

# dash.register_page(__name__)
dash.register_page(__name__, title='app2', order=2, meta_tags=[{'name': 'viewport',
                        'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}])
#read file
dfcorr = pd.read_csv('assets/mystocks-corr.csv')

#for datepicker
dfcorr['Date'] = pd.to_datetime(dfcorr['Date'])

dfcorr['Date2']= dfcorr['Date'] # duplicate a copy of date column to adjust min, max of datepicker
dfcorr['Date2'] = dfcorr['Date2'].dt.date 

dfcorr.set_index('Date', inplace=True)

#adjust min, max of datepicker
min_date = dfcorr.Date2.unique().min()
min_date_y = min_date.year #print(min_date.year)
min_date_m = min_date.month
min_date_d = min_date.day
max_date = dfcorr.Date2.unique().max()
max_date_y = max_date.year #print(min_date.year)
max_date_m = max_date.month
max_date_d = max_date.day
del dfcorr['Date2']

#set up correl matrix
corr_matrix = dfcorr.corr()



def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [ 
                    html.P("Select Stock Ticker:",
                    style={"textDecoration": "underline", 'marginTop':60}),
                    dcc.Dropdown(
                        id='stockdropdown',
                        multi=True,
                        value=['DIA','SPY','AMZN'],
                        clearable=False,
                        options=[{'label': x, 'value': x} for x in dfcorr.columns              
        ])
                ], xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            dbc.Col(
                [
                    html.P("Select Period:",
                    style={"textDecoration": "underline", 'marginTop':60}),
                    dcc.DatePickerRange(id='my-date-picker-range',  # ID to be used for callback
                                        calendar_orientation='horizontal',  # vertical or horizontal
                                        day_size=39,  # size of calendar image. Default is 39
                                        end_date_placeholder_text="Return",  # text that appears when no end date chosen
                                        with_portal=False,  # if True calendar will open in a full screen overlay portal
                                        first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
                                        reopen_calendar_on_clear=True,
                                        is_RTL=False,  # True or False for direction of calendar
                                        clearable=True,  # whether or not the user can clear the dropdown
                                        number_of_months_shown=1,  # number of months shown when calendar is open
                                        min_date_allowed=dt(min_date_y,min_date_m,min_date_d),  
                                        max_date_allowed=dt(max_date_y, max_date_m, max_date_d),  
                                        initial_visible_month=dt(max_date_y, max_date_m, max_date_d),  
                                        start_date=dt(min_date_y, 12, 1).date(),
                                        end_date=dt(max_date_y, max_date_m, max_date_d).date(),
                                        display_format='MMM Do, YY',
                                        month_format='MMMM, YYYY', 
                                        minimum_nights=2, 
                                        persistence=True,
                                        persisted_props=['start_date'],
                                        persistence_type='session',  
                                        updatemode='singledate'),
                ], xs=4, sm=4, md=6, lg=6, xl=6, xxl=6),
        ], align='center'),
        
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='heatmap', figure={})  
        ], 
        xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
    ]),                
])

# Create interactivity between components and graph
@callback(
    Output('heatmap', 'figure'),
    Input('stockdropdown', 'value'),
    [Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date')]
)

def plot_data(stock_slctd, start_date, end_date):
    for x in stock_slctd:
        dfnewtwo = dfcorr[stock_slctd]
        dff = dfnewtwo.loc[start_date:end_date]
        corr_matrixtwo = dff.corr()
    #return corr_matrixtwo
    
    #heatmap for correl matrix
    fig = px.imshow(round(corr_matrixtwo,4), text_auto=True, color_continuous_scale='greens')
    fig.update_layout(height=900, width=900)
       
    return fig
