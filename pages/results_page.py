from dash.dependencies import Input, Output, State
import numpy as np
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd


results_page = dbc.Container([
    dbc.Row([
        dbc.Row([
            dbc.Row([
                dbc.Row([
                    dbc.Row([
                        dbc.Col([], width=5),

                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Row([
                                dbc.Col(width=3),
                                dbc.Col([html.Br(), html.H3('Most popular names ever')], width=6),
                                html.Div(id='average-rating-over-time-graph')
                            ])
                        ], width=6),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col(width=2),
                                dbc.Col([html.Br(), html.H3('Most birthgiving reagions overall')], width=8),
                                html.Div(id='average-rating-by-category-graph')
                            ])
                        ], width=6)
                    ], id='average-rating-over-time')
                ], id='average-rating-by-category'),
                dbc.Row([
                    dbc.Row([
                        dbc.Col([], width=5),

                    ]),
                    dbc.Row([
                        dbc.Row([
                            dbc.Col([], width=3),
                        ]),
                        dbc.Row([
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col(width=3),
                                    dbc.Col([html.Br(), html.H3('Most popular name for each available year.')], width=6),
                                    html.Div(id='average-rating-by-top-categories-graph')
                                ])
                            ], id='average-rating-by-top-categories', width=6),
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col(width=3),
                                    dbc.Col([html.Br(), html.H3('Most popular name for each available year.')], width=6),
                                    html.Div(id='average-rating-by-top-categories-graph1')
                                ])
                            ],id='average-rating-by-top-categories1', width=6),
                        ])
                    ])
                ]),
            ]),
        ]),
        dbc.Row([
            dbc.Row([
                dbc.Row([
                    dbc.Row([
                        dbc.Col([], width=5),
                        dbc.Col([html.Br(), html.H2('Density of the population')], width=6)
                    ]),
                    dbc.Row([
                        dbc.Col(width=3),
                        dbc.Col([
                            html.Div(id='counts-over-time-graph')
                        ], width=6)
                    ])
                ], id='counts-over-time'),
            ]),
        ])
    ]),
], id='overview-page', style={'maxWidth':'100%'})

