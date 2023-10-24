from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash_extensions.enrich import Output, DashProxy, Input, MultiplexerTransform, html
from pages import map_layout

app = DashProxy(transforms=[MultiplexerTransform()], external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    map_layout.layout(),
    dbc.Button("Left", id="left"),
    dbc.Button("Right", id="right"),
    html.Div(id="log")
])

@app.callback(Output("log", "children"), Input("left", "n_clicks"))
def left(n_clicks):
    if not n_clicks:
        raise PreventUpdate()
    return "left"

@app.callback(Output("log", "children"), Input("right", "n_clicks"))
def right(n_clicks):
    if not n_clicks:
        raise PreventUpdate()
    return "right"

if __name__ == "__main__":
    app.run_server(debug=True)