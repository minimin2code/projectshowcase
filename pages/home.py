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
                 'and self improvement. A crypto enthusiast and a geek at heart, I am also \n'
                 'currently learning about NFTs, React Native for mobile app development and\n' 
                 'Dash. Love a good sweat and I trust that good things come to those who sweat.\n' 
                 'Absolutely love coding.',
                 style={'textAlign': 'center', 'white-space': 'pre'}, className='ms-3'),
                

    dcc.Markdown('### Skills', style={'textAlign': 'center'}, className='row'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Risk analysis
            * Risk attribution
            * Portfolio management
            * Data analytics
            * Investment compliance
            * Financial Modeling
            ''')
        ], width={"size": 3, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            * VBA
            * Python
            * HTML
            * CSS
            * Bloomberg
            * Tableau
            ''')
        ], width=3)
    ], justify='center'),

    # dcc.Markdown('### Work History', style={'textAlign': 'center'}),
    # html.Hr(),

    # dbc.Row([
    #     dbc.Col([
    #         dcc.Markdown('03/2018 to current', style={'textAlign': 'center'})
    #     ], width=2),
    #     dbc.Col([
    #         dcc.Markdown('Senior Sales Associate \n'
    #                      'Bed Bath & Beyond Inc - New York, NY',
    #                      style={'white-space': 'pre'},
    #                      className='ms-3'),
    #         html.Ul([
    #             html.Li('Applied security and loss prevention training toward recognizing risks and reducing store theft'),
    #             html.Li('Trained and developed sales team associates in products, selling techniques and procedures'),
    #             html.Li('Maintained organized, presentable merchandise to drive continuous sales'),
    #             html.Li('Implemented up-selling strategies for recommending accessories and couplementary purchases')
    #         ])
    #     ], width=5)
    # ], justify='center'),

    # dbc.Row([
    #     dbc.Col([
    #         dcc.Markdown('06/2017 to 03/2018',
    #                      style={'textAlign': 'center'})
    #     ], width=2),
    #     dbc.Col([
    #         dcc.Markdown('Sales Associate \n'
    #                      'Target - New York, NY',
    #                      style={'white-space': 'pre'},
    #                      className='ms-3'),
    #         html.Ul([
    #             html.Li(
    #                 'Maintained organized, presentable merchandise to drive continuous sales'),
    #             html.Li(
    #                 'Trained and developed sales team associates in products, selling techniques and procedures'),
    #             html.Li(
    #                 'Organized racks and shelves to maintain store visual appeal, engage customers and promote merchandise'),
    #             html.Li(
    #                 'Implemented up-selling strategies for recommending accessories and couplementary purchases')
    #         ])
    #     ], width=5)
    # ], justify='center'),

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
