from dash.dependencies import Input, Output, State
# import numpy as np
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
# import plotly.express as px
import json
# from glob import glob
# from config import find_button_clicks#, movie_finder
# from collections import OrderedDict
import plotly.figure_factory as ff
import datetime
import folium


data = pd.read_parquet("data/shnik_2021.parquet")
data["tariq"] = datetime.date.today().year - data.tari
arm_population = pd.read_csv("data/arm_population.csv")
armenia_border = json.load(open("data/geo/gadm36_ARM_1.json"))
def register_find_name_page_callbacks(app):
    @app.callback(Output('qaq', 'children'),
                  Input('find-movie-btn', 'n_clicks'),
                  State('movie-input', 'value'))
    def find_plot(c, input):
        graphs = []
        if c and input and len(input):
            data1 = data[data["anun"].str.lower() == input.lower()]


            d = data1.groupby(["marz"])["anun"].count()
            arm_population1 = arm_population.merge(d, left_on=["province_arm"], right_on="marz")

            m = folium.Map(location=[40.2, 44.6], zoom_start=7.2)
            folium.Choropleth(geo_data=armenia_border, data=arm_population1[:-1],
                              columns=["province_eng", "anun"],
                              fill_color='OrRd',
                              key_on="feature.properties.NAME_1",
                              fill_opacity=0.7, line_opacity=0.2,
                              highlight=True, nan_fill_color="white"
                              ).add_to(m)
            loc = 'Most popular birth region outside of Yerevan.'
            title_html = '<h3 align="center" style="font-size:16px"><b>{}</b></h3>'.format(loc)

            m.get_root().html.add_child(folium.Element(title_html))

            m.save("../map.html")

            with open("../map.html", "r") as f:
                m = f.read()

            graph1= html.Iframe(id="map", srcDoc=m, width="100%", height="600")
            #

            gb_marz = data1.groupby("marz")["marz"].count()
            fig = go.Figure([go.Bar(x=gb_marz.index, y=gb_marz)])
            fig.update_layout(xaxis={'categoryorder': 'total descending'})
            fig.update_layout(title={'text': "Most popular birth region", 'x': 0.5}, xaxis_title="region",yaxis_title="count")
            graph2 = dcc.Graph(figure=fig)

            a = data1.groupby("amis")["anun"].count()
            fig = go.Figure([go.Bar(x=a.index, y=a.values)])
            fig.update_layout(xaxis={'categoryorder': 'total descending'})
            fig.update_layout(title={'text': "Most popular birth month", 'x': 0.5}, xaxis_title="month", yaxis_title="count")
            graph3 = dcc.Graph(figure=fig)

            d = data1.groupby("tari")["anun"].count()
            fig = go.Figure(go.Scatter(x=d.index, y=d.values, mode='lines+markers', name='lines+markers'))
            fig.update_layout(title={'text': "Number of people born with the name", 'x': 0.5}, xaxis_title="year",yaxis_title="count")
            graph4 = dcc.Graph(figure=fig)

            d = data1["azganun"].value_counts().head(10)
            fig = go.Figure([go.Bar(x=d.index, y=d.values)])
            fig.update_layout(xaxis={'categoryorder': 'total descending'})
            fig.update_layout(title={'text': "Most popular surename", 'x': 0.5}, xaxis_title="surename", yaxis_title="count")
            graph5 = dcc.Graph(figure=fig)

            fig = ff.create_distplot([data1["tariq"]], ["tariq"], show_rug=False)
            fig.update_layout(showlegend=False)
            fig.update_layout(title={'text': "Age distribution", 'x': 0.5}, xaxis_title="age", yaxis_title="density")
            graph6 = dcc.Graph(figure=fig)

            graphs = [
                dbc.Row([
                    dbc.Col([graph1], width=6),
                    dbc.Col([graph2], width=6),
                ]),
                dbc.Row([
                    dbc.Col([graph3], width=6),
                    dbc.Col([graph4], width=6),
                ]),
                dbc.Row([
                    dbc.Col([graph5], width=6),
                    dbc.Col([graph6], width=6),
                ])
            ]
        return graphs


    # @app.callback([Output('top-movie-1', 'children'),
    # Output('top-movie-2', 'children'),
    # Output('top-movie-3', 'children')],
    # [Input('find-movie-page', 'children')])
    # def init_top_movies(children):
    #
    #     movies = []
    #     for i, movie in enumerate(movie_finder.top_movies):
    #         overview_text = ', '.join([m['name'] for m in movie['cast'][:5]])
    #         movies.append([
    #             dbc.CardImg(src=movie['image'], top=True),
    #             dbc.CardBody([
    #                     html.H5(movie['title'], className="card-title"),
    #                     html.P([html.B('Cast: '), overview_text]),
    #                     dbc.Button("Find", color="primary", id=f'top-movie-{i+1}-find-btn', n_clicks=0),
    #                 ]
    #             )
    #         ])
    #
    #     return movies
    #
    # @app.callback(Output('tabs-graph', 'value'),
    # [Input('placeholder', 'children'),
    # Input('top-movie-1-find-btn', 'n_clicks'),
    # Input('top-movie-2-find-btn', 'n_clicks'),
    # Input('top-movie-3-find-btn', 'n_clicks'),
    # Input('find-movie-btn', 'n_clicks')],
    # [State('movie-input', 'value'),
    # State('search-by-dropdown', 'value'),
    # State('min-movie-year-input', 'value'),
    # State('max-movie-year-input', 'value'),
    # State('min-movie-rating-input', 'value'),
    # State('limit-search-input', 'value'),
    # State('fuzzy-match-checkbox', 'value')])
    # def find_movie_click(_, t1_btn, t2_btn, t3_btn, find_btn, input, *args):
    #     t = None
    #     if find_button_clicks[1] != t1_btn:
    #         t = 1
    #         find_button_clicks[1] = t1_btn
    #     elif find_button_clicks[2] != t2_btn:
    #         t = 2
    #         find_button_clicks[2] = t2_btn
    #     elif find_button_clicks[3] != t3_btn:
    #         t = 3
    #         find_button_clicks[3] = t3_btn
    #     elif find_button_clicks[-1] != find_btn:
    #         t = -1
    #         find_button_clicks[-1] = find_btn
    #
    #     options = dict(zip(['input', 'search_by', 'min_year', 'max_year', 'min_rating', 'limit', 'fuzzy'], [input]+list(args)))
    #     if not options['search_by']:
    #         options['search_by'] = ['Title']
    #
    #     tab = 'find-movie-tab'
    #     if t and t > 0:
    #         tab = 'search-result-tab'
    #         movie_finder.find_movie(top_movie_num=t, **options)
    #     elif t == -1 and input:
    #         tab = 'results-tab'
    #         movie_finder.find_movie(top_movie_num=t, **options)
    #
    #         inputs = [Input(f'go-to-movie-page-button-{i}', 'n_clicks') for i in range(len(movie_finder.search_results))]
    #
    #         print('VVVVVVVVVVV')
    #         @app.callback(Output('placeholder', 'children'), inputs)
    #         def init_movie_buttons(*btns):
    #             print(btns)
    #
    #             return None
    #         print('ZZZZZZZZZZZZZ')
    #
    #         print('AAAA', len(movie_finder.search_results))
    #
    #     elif not t and find_btn:
    #         # print(movie_finder.found_movie)
    #         print('AAAAA')
    #         tab = 'search-result-tab'
    #
    #     return tab
    #
    #
    # @app.callback(
    #     [Output("advanced-collapse", "is_open"),
    #     Output("advanced-collapse-button", "children")],
    #     [Input("advanced-collapse-button", "n_clicks")],
    #     [State("advanced-collapse", "is_open"),
    #     State("advanced-collapse-button", "children")],
    # )
    # def toggle_collapse(n, is_open, children):
    #
    #     class_name = children[1]['props']['className']
    #     if class_name == 'fa-solid fa-angle-down':
    #         class_name = 'fa-solid fa-angle-up'
    #     else:
    #         class_name = 'fa-solid fa-angle-down'
    #
    #     children = [children[0], html.I(className=class_name)]
    #
    #     if n:
    #         return not is_open, children
    #     return is_open, children


        

        