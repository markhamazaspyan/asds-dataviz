from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# find_movie_page = dbc.Container([])


find_name_page = dbc.Container([
    html.Label('', id='placeholder'),
    html.Br(),
    dbc.Row([
        dbc.Col(width=4),
        dbc.Col([
            dbc.Row([
                dbc.Row([html.Br(), dbc.Label('Enter a name in Armenian.', style={'fontSize':'24px'})]),
                dbc.Row([
                    dbc.Col([dbc.Input(id='movie-input', style={'fontSize':'24px'})], width=8),
                    dbc.Col([dbc.Button('Find', id='find-movie-btn', n_clicks=0, style={'fontSize':'24px', 'textAlign':'center'})], width=4)
                ])
            ]),
            html.Br(),
        ], width=4),
    ]),
    dbc.Row(id='qaq')
], id='find-movie-page', style={'maxWidth':'100%'})