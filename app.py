import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])

#add in from video
server = app.server
header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Nav([
                        dbc.NavLink(page["name"], href=page["path"])
                        for page in dash.page_registry.values()
                        if not page["path"].startswith("/app")
                    ])
            ])
        ],
        fluid=True,
    ),
    dark=True,
    color='primary'
)

app.layout = dbc.Container([header, dash.page_container], fluid=False)

if __name__ == '__main__':
	#app.run_server()
    app.run_server(host='localhost',port=8050)