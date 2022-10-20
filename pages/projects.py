import dash
from dash import html, dcc, Input, Output, dash_table, State, callback  
import dash_bootstrap_components as dbc                #
import pandas as pd
from .side_bar import sidebar

import matplotlib.pyplot as plt             # pip install matplotlib
import mpld3                                # pip install mpld3
import matplotlib.mlab as mlab
import plotly.express as px
import seaborn as sns
sns.set()
import datetime
from datetime import datetime as dt
import matplotlib.dates as mdates

import numpy as np
from scipy.stats import norm

dash.register_page(__name__, title='App1', order=1)

df = pd.read_csv('assets/mystocks.csv')

df['Return'] = df.groupby('Symbols')['Close'].pct_change()
df['%Return'] = df['Return'].multiply(100)

#for datepicker
df['Date'] = pd.to_datetime(df['Date'])
df['Date2']= df['Date'] # duplicate a copy of date column to adjust min, max of datepicker
df['Date2'] = df['Date2'].dt.date # duplicate a copy of date column to adjust min, max of datepicker
df.set_index('Date', inplace=True)

# duplicate a copy of date column to adjust min, max of datepicker
min_date = df.Date2.unique().min()
min_date_y = min_date.year #print(min_date.year)
min_date_m = min_date.month
min_date_d = min_date.day
max_date = df.Date2.unique().max()
max_date_y = max_date.year #print(min_date.year)
max_date_m = max_date.month
max_date_d = max_date.day


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
                   html.P("Select Stock Ticker:",style={"textDecoration": "underline", 'marginTop':60}),
                   dcc.Dropdown(id='stockdropdown',
                                value='AMZN',
                                clearable=False,
                                options=[{'label': x, 'value': x} for x in sorted(df['Symbols'].unique())]), 
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),
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
                ], xs=4, sm=4, md=8, lg=8, xl=8, xxl=8),
        ], align='center'),
        
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='line-grp', figure={})  # here is where we will put the graph we make
        ], width=12)
    ]),

    dbc.Row([
          dbc.Col([
            #dbc.Label('Return Distribution'),
            dcc.Graph(id='bar-grp', figure={})  # here is where we will put the returns graph we
        ], width=8),
        
        
          dbc.Col([
            dbc.Label('Statistical Summary:'),
            html.Div(id='table-placeholder2', children=[])
        ], width=4)
        
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='scatter-grp2', figure={})  # here is where we will put the graph we make
        ], width=12)
    ])
                
])


# Create interactivity between components and graph
@callback(
    #Output('scatter-grp', 'srcDoc'),
    Output('scatter-grp2', 'figure'),
    Output('line-grp', 'figure'),
    Output('bar-grp', 'figure'),
    #Output('bar-grp', 'srcDoc'),
    Output('table-placeholder2', 'children'),
    Input('stockdropdown', 'value'),
    #Input('range-slider', 'value')
    [Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date')]
)

def plot_data(selected_stock,start_date, end_date):

    # filter data based on user selection
    df3 = df[df.Symbols == selected_stock]
    dff = df3.loc[start_date:end_date]


    # compute statistics
    avr_rtn = dff.Return.mean() * 100
    stdev = dff.Return.std() *100
    sharpe = avr_rtn/stdev
    max_rtn = dff.Return.max() *100
    min_rtn = dff.Return.min() *100
    hsvar = dff.Return.quantile(0.01) *100
    pvar = norm.ppf(0.01,avr_rtn,stdev)
    skew = dff.Return.skew()
    kurtosis = dff.Return.kurtosis()
    tloss = sum(dff.Return[dff.Return<hsvar/100])
    tlen = len(dff.Return[dff.Return<hsvar/100])
    csvar = tloss/tlen * 100
    
    stat_data = {'Measure': ['Average_Daily_Rtn(%)', 'Daily_Volatility(%)', 'Rtn/Vol Ratio',
                             'Max_Rtn(%)','Min_Rtn(%)','Historical VaR(99%)','Parametric VaR(99%)',
                             'Expected Shortfall','Skewness', 'Kurtosis'],
        'Value': [round(avr_rtn,4), round(stdev,4), round(sharpe,4), round(max_rtn,4), round(min_rtn,4),
                  round(hsvar,4), round(pvar,4), round(csvar,4), round(skew,4),round(kurtosis,4)]}
  
    # Create DataFrame for statistical summary table
    dff2 = pd.DataFrame(stat_data)
   
    # build scatter plot
    #dates = [pd.to_datetime(d) for d in dff.Date]
    

    
    #scatter plot with px
    scatterplot = px.scatter(
    data_frame=dff,
    x=dff.index,
    y='%Return',
    labels={"Return":"Daily Return(%)"},  # map the labels
    title='Scatter plot of daily return',           # figure title
    width=1200,                  # figure width in pixels
    height=500,                # igure height in pixels
    template='plotly_white',     # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                # 'plotly_white', 'plotly_dark', 'presentation',
                                # 'xgridoff', 'ygridoff', 'gridon', 'none'
    opacity=0.9,                # set opacity of markers
    )
        
    
    #line grp
    html_line = px.line(dff, x=dff.index, y='Close')
    
    html_line.update_xaxes(
    rangeslider_visible=True,
)
    
    html_line.update_layout(
    #plot_bgcolor='white'
    template='plotly_white',
)

    # HISTOGRAM
    fig_hist = px.histogram(dff, x="%Return", histnorm='probability density',nbins=60)
    fig_hist.update_layout(bargap=0.1,
                          template='plotly_white')

    
    # build DataTable
    mytable2 = dash_table.DataTable(
        id='tabl',
        columns=[{"name": i, "id": i} for i in dff2.columns],
        data=dff2.to_dict('records'),
    )
    
        # build DataTable
    mytable = dash_table.DataTable(
        id='tabl2',
        columns=[{"name": i, "id": i} for i in dff.columns],
        data=dff.to_dict('records'),
    )
    
    return scatterplot, html_line, fig_hist, mytable2