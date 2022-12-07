import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)

# resume sample template from https://zety.com/
layout = html.Div([
    dcc.Markdown('# Celeste', style={'textAlign':'center'}, className='row'),
    dcc.Markdown('Singapore', style={'textAlign': 'center'}, className='row'),

    dcc.Markdown('### About Me', style={'textAlign': 'center'},className='row'),
    html.Hr(),
    dcc.Markdown('I am an investment risk manager with a penchant for continuous learning \n'
                 'and self improvement. A crypto enthusiast and a geek at heart, I am also currently \n'
                 'learning Dash and React Native for mobile app development. \n' 
                 'Love a good sweat and I trust that good things come to those who sweat. \n' 
                 'Absolutely love coding.',
                 style={'textAlign': 'center', 'white-space': 'pre'}, className='ms-3'),
                

    dcc.Markdown('### Skills', style={'textAlign': 'center'}, className='row'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Market risk analysis 
            * Performance and risk attribution
            * Portfolio management
            * Data analytics
            * Risk and compliance
            ''')
        ], width={"size": 3, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            * VBA
            * Python
            * HTML, CSS
            * Bloomberg
            * Tableau
            ''')
        ], width=3)
    ], justify='center'),



    dcc.Markdown('### Education', style={'textAlign': 'center'}, className='row'),
    html.Hr(),

    dbc.Row([
        # dbc.Col([
        #     dcc.Markdown('2014',
        #                  style={'textAlign': 'center'})
        # ], width=2),
        dbc.Col([
            dcc.Markdown('MSc Quantitative Finance\n'
                         'City University of London - United Kingdom',
                         style={'white-space': 'pre'},
                         className='row'), #className='ms-3'
        ], width=5)
    ], justify='center'),
], className='ten columns offset-by-one')

