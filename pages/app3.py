#import necessary lib
import dash  # (version 1.11.0)
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import datetime

import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import datetime
import numpy as np
import yfinance as yf

from .side_bar import sidebar

dash.register_page(__name__)



def layout():
    return html.Div([

        html.Div([
            html.P(id='header',style={"font-size": 20}),
            html.P(id='headerTwo',style={"font-weight": "bold", "font-size": 50}),
            ],style={'marginLeft': 50, 'marginTop': 30, 'text-transform': 'uppercase'}),

        html.Div([
        dcc.Input(
            id='fxOne',
            type='text',
            debounce=False,    # changes to input are sent to Dash server only on enter or losing focus
            #pattern=rA-Za-z].*",  # Regex: string must start with letters only
            inputMode='latin',       # provides a hint to browser on type of data that might be entered by the user.
            name='text',             # the name of the control, which is submitted with the form data
            list='browser',          # identifies a list of pre-defined options to suggest to the user
            autoFocus=True,          # the element should be automatically focused after the page loaded
            value= 'USD',
            style={'height': 30, 'width': 240, 'marginLeft':50, 'text-transform': 'uppercase'},
        ),
    ]),
    
    html.Br(),
    
    html.Div([
        dcc.Input(
            id='fxTwo',
            type='text',
            debounce=False,          # changes to input are sent to Dash server only on enter or losing focus
            inputMode='latin',       # provides a hint to browser on type of data that might be entered by the user.
            name='text',             # the name of the control, which is submitted with the form data
            list='browser',          # identifies a list of pre-defined options to suggest to the user
            autoFocus=True,          # the element should be automatically focused after the page loaded
            value= 'SGD',
            style={'height': 30, 'width': 240, 'marginLeft':50, 'text-transform': 'uppercase'},
            #size=80
 
        ),
    ]),   
    

    html.Br(),
    html.Br(),

    dcc.Graph(id="mygrp"),
    
    
])

# Create interactivity between components and graph
@callback(
    Output(component_id='mygrp', component_property='figure'),
    Output(component_id='header', component_property='children'),
    Output(component_id='headerTwo', component_property='children'),
    [Input(component_id='fxOne', component_property='value'),
     Input(component_id='fxTwo', component_property='value'),
     ]
)

def plot_data(fxOne, fxTwo):
    
    z=fxOne+fxTwo+'=X'

    forex_spot = round(yf.download([z], period='1d', interval='15m')['Close'][-1],4)
    #timestamp = forex_spot.index[-1]
    
    forex_data = yf.download([z], period='740d', interval='1d')['Close']

    
    #line grp
    html_line = px.line(forex_data, x=forex_data.index, y='Close')
    
    html_line.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=2, label="2y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
  
    html_line.update_layout(
    #plot_bgcolor='white'
    template='plotly_white',
)
    
    # create statement to return to dashboard
    statement = '1 ' + fxOne + ' = ',
    statementTwo = str(forex_spot) +' '+ fxTwo
            
    
    return html_line, statement, statementTwo