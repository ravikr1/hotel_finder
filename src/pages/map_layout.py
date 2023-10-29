from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash_extensions.enrich import Output, DashProxy, Input, MultiplexerTransform, html
from dash import get_asset_url


def layout():
    return html.Div(
        [
            html.Iframe(id="test-frame", src=get_asset_url("map.html"),style={"height": "1067px", "width": "100%"}),
        ]
    )
