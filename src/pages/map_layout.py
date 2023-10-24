from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash_extensions.enrich import Output, DashProxy, Input, MultiplexerTransform, html


def layout():
    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                   
                )
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        )
    )