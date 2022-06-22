import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output, State
import os
from callbacks import register_results_page_callbacks, register_find_name_page_callbacks#, , register_movie_page_callbacks
from pages import  find_name_page, results_page


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
register_find_name_page_callbacks(app)
register_results_page_callbacks(app)

app.layout = html.Div([
    html.H1('Armenian name demographic analysis.', style={'textAlign': 'center'}),
    dcc.Tabs(id="tabs-graph", value='results-tab', children=[
        # dcc.Tab(overview_page, label='Overview', value='overview-tab', style={'fontSize': '32px'}, selected_style={'fontSize': '32px'}),
        dcc.Tab(results_page, label='Statistics about Names', value='results-tab', style={'fontSize': '32px'}, selected_style={'fontSize': '32px'}),
        dcc.Tab(find_name_page, label='Search by name', value='find-movie-tab', style={'fontSize': '32px'}, selected_style={'fontSize': '32px'}),
        # dcc.Tab(movie_page, label='Movie', value='search-result-tab', style={'fontSize': '32px'}, selected_style={'fontSize': '32px'}),
    ]),
    html.Br(),
    html.Div(id="page-content")
])


if __name__ == "__main__":
    app.run_server(debug=True, port=os.getenv('PORT', 3000))