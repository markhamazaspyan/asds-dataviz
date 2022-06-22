from dash.dependencies import Input, Output, State
import numpy as np
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
# import folium
import plotly


# data = pd.read_parquet("data/shnik_2021.parquet")
def register_results_page_callbacks(app):

#################### AVERAGE RATING ####################
    @app.callback(Output('average-rating-over-time-graph', 'children'),
        [Input('average-rating-over-time', 'children')])
    def init_average_rating(children):

        # data['azganun_anun_haeranun'] = data.azganun + " " + data.anun + " " + data.haeranun
        # un_p = data["azganun_anun_haeranun"].value_counts().head()
        # fig = go.Figure([go.Bar(x=un_p.index, y=un_p)])
        # fig.update_layout(xaxis={'categoryorder': 'total descending'},yaxis_title="count")

        # fig.show()
        fig = plotly.io.read_json("data/graph1.json")
        graph = dcc.Graph(figure=fig)

        return graph


    @app.callback(Output('average-rating-by-category-graph', 'children'),
        [Input('average-rating-by-category', 'children')])
    def init_average_rating_by_category(children):

        # gb_marz = data.groupby("marz")["marz"].count()
        # fig = go.Figure([go.Bar(x=gb_marz.index, y=gb_marz)])
        # fig.update_layout(xaxis={'categoryorder': 'total descending'},yaxis_title="count")
        fig = plotly.io.read_json("data/graph2.json")
        graph = dcc.Graph(figure=fig)

        return graph
#
#
    @app.callback(Output('average-rating-by-top-categories-graph', 'children'),
        [Input('average-rating-by-top-categories', 'children')])
    def init_average_rating_by_top_categories(children):
        # dic = {}
        # for i in data.tari.unique():
        #     dic[i] = data[data.tari == i].anun.value_counts().index[0]
        #
        # db = pd.DataFrame([dic]).T.reset_index()
        #
        # db.columns = ["year", "name"]
        #
        # db = db.sort_values(by="year")
        #
        # db["year_end"] = db.year + 1
        #
        # db.year = db.year.astype(str)
        # db.year_end = db.year_end.astype(str)
        #
        # fig = px.timeline(db, x_start="year_end", x_end="year", y="name")
        fig = plotly.io.read_json("data/graph3.json")
        graph = dcc.Graph(figure=fig)

        return graph


    @app.callback(Output('average-rating-by-top-categories-graph1', 'children'),
        [Input('average-rating-by-top-categories1', 'children')])
    def init_average_rating_by_top_categories(children):
        # gb_marz = data.groupby("marz")["marz"].count()
        # fig = go.Figure([go.Bar(x=gb_marz.index, y=gb_marz)])
        # fig.update_layout(xaxis={'categoryorder': 'total descending'})
        # fig = plotly.io.read_json("data/graph3.json")
        graph = html.Iframe(src="https://public.flourish.studio/visualisation/6667677/", width="100%", height="500")

        return graph

#
#
#
    # @app.callback([Output('average-rating-category-dropdown', 'options'),
    #     Output('average-rating-category-dropdown', 'value')],
    #     [Input('average-rating-category-dropdown-col', 'children')])
    # def init_average_rating_dropdown_options(children):
    #     df = pd.read_csv('data/overview.csv')
    #     all_genres = df['genre'].unique().tolist()
    #     top_genres = ['Comedy', 'Fantasy', 'Drama', 'Horror', 'Documentary', 'Action']
    #
    #     return all_genres, top_genres
#
# #################### COUNTS ####################
    @app.callback(Output('counts-over-time-graph', 'children'),
        [Input('counts-over-time', 'children')])
    def init_counts(children):
        with open("data/overview_map.html", "r") as f:
            m=f.read()

        return html.Iframe(id="map", srcDoc=m,width="100%",height="600")
#
#
#     @app.callback(Output('counts-by-category-graph', 'children'),
#         [Input('counts-by-category', 'children'),
#         Input('counts-category-dropdown', 'value')])
#     def init_counts_by_category(children, selected_genres):
#         df = pd.read_csv('data/overview.csv')
#
#         fig = go.Figure()
#         if len(selected_genres):
#             tmp_df = df[df['genre'].isin(selected_genres)]
#             tmp_df = tmp_df.sort_values(by="year")
#             tmp_df = tmp_df.groupby(['year', 'genre']).sum().reset_index()
#
#             fig = px.bar(tmp_df, x='year', y="count", color='genre')
#             fig.update_layout({
#                 'title': 'Number of movies per category over the years',
#                 'xaxis_title': 'Year',
#                 'yaxis_title': 'Count',
#             })
#
#         graph = dcc.Graph(figure=fig)
#
#         return graph
#
#
#     @app.callback(Output('counts-by-top-categories-graph', 'children'),
#         [Input('counts-by-top-categories', 'children'),
#         Input('counts-category-dropdown', 'value')])
#     def init_counts_by_top_categories(children, selected_genres):
#         df = pd.read_csv('data/overview.csv')
#
#         fig = go.Figure()
#         if len(selected_genres):
#             tmp_df = df[df['genre'].isin(selected_genres)]
#             tmp_df = tmp_df.sort_values(by="year")
#             fig = px.scatter(tmp_df, x='year', y="count", facet_col='genre', trendline='ols', trendline_color_override='red')
#
#             fig.update_layout({
#                 'title': 'Number of movies per category over the years',
#                 'xaxis_title': 'Year',
#                 'yaxis_title': 'Average rating',
#             })
#
#         graph = dcc.Graph(figure=fig)
#
#         return graph
#
#
#     @app.callback([Output('counts-category-dropdown', 'options'),
#         Output('counts-category-dropdown', 'value')],
#         [Input('counts-category-dropdown-col', 'children')])
#     def init_counts_dropdown_options(children):
#         df = pd.read_csv('data/overview.csv')
#         all_genres = df['genre'].unique().tolist()
#         top_genres = ['Comedy', 'Fantasy', 'Drama', 'Horror', 'Documentary', 'Action']
#
#         return all_genres, top_genres
#
#
#
# #################### AVERAGE REVENUE ####################
#     @app.callback(Output('average-revenue-over-time-graph', 'children'),
#         [Input('average-revenue-over-time', 'children')])
#     def init_average_revenue(children):
#         df = pd.read_csv('data/overview.csv')
#
#         fig = go.Figure()
#
#         fig.add_trace(go.Scatter(x=df['date'], y=df['revenue_average'], name='Average revenue'))
#         fig.add_trace(go.Scatter(x=df['date'], y=[df['revenue_average'].mean()]*df.shape[0], name='Mean'))
#         fig.update_layout({
#             'xaxis_title': 'Date',
#             'yaxis_title': 'Average revenue',
#         })
#
#         graph = dcc.Graph(figure=fig)
#
#         return graph
#
#
#     @app.callback(Output('average-revenue-by-category-graph', 'children'),
#         [Input('average-revenue-by-category', 'children'),
#         Input('average-revenue-category-dropdown', 'value')])
#     def init_average_revenue_by_category(children, selected_genres):
#         df = pd.read_csv('data/overview.csv')
#
#         fig = go.Figure()
#         if len(selected_genres):
#             tmp_df = df[df['genre'].isin(selected_genres)]
#             tmp_df = tmp_df.sort_values(by="year")
#             tmp_df = tmp_df.groupby(['year', 'genre']).mean().reset_index()
#
#             fig = px.bar(tmp_df, x='year', y="revenue_average", color='genre')
#             fig.update_layout({
#                 'title': 'Average revenue per category over the years',
#                 'xaxis_title': 'Year',
#                 'yaxis_title': 'Average revenue',
#             })
#
#         graph = dcc.Graph(figure=fig)
#
#         return graph
#
#
#     @app.callback(Output('average-revenue-by-top-categories-graph', 'children'),
#         [Input('average-revenue-by-top-categories', 'children'),
#         Input('average-revenue-category-dropdown', 'value')])
#     def init_average_revenue_by_top_categories(children, selected_genres):
#         df = pd.read_csv('data/overview.csv')
#
#         fig = go.Figure()
#         if len(selected_genres):
#             tmp_df = df[df['genre'].isin(selected_genres)]
#             tmp_df = tmp_df.sort_values(by="year")
#             fig = px.scatter(tmp_df, x='year', y="revenue_average", facet_col='genre', trendline='ols', trendline_color_override='red')
#
#             fig.update_layout({
#                 'title': 'Average revenue per category over the years',
#                 'xaxis_title': 'Year',
#                 'yaxis_title': 'Average revenue',
#             })
#
#         graph = dcc.Graph(figure=fig)
#
#         return graph
#
#
#
#     @app.callback([Output('average-revenue-category-dropdown', 'options'),
#         Output('average-revenue-category-dropdown', 'value')],
#         [Input('average-revenue-category-dropdown-col', 'children')])
#     def init_average_revenue_dropdown_options(children):
#         df = pd.read_csv('data/overview.csv')
#         all_genres = df['genre'].unique().tolist()
#         top_genres = ['Comedy', 'Fantasy', 'Drama', 'Horror', 'Documentary', 'Action']
#
#         return all_genres, top_genres