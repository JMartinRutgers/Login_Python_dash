import dash
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
# from flask_login.utils import login_required
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


colors = {
    'background': '#42d7f5',
    'text': '#FFFFFF'
}


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash/")
    dash_app.layout = html.Div(style={'backgroundColor': colors['background']},
        children=[
            html.H1(children="Dashboard Dash/python",
              style={
            'textAlign': 'center',
            'color': colors['text']
        }),
            html.Div(
                children=""" Dash: A web application framework for Python.""", style={
                'textAlign': 'center',
                'color': colors['text']
    }),
            dcc.Graph(
                id="example-graph",
                figure=px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
            )
        ]
    )


    return dash_app