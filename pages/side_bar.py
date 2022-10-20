import dash
from dash import html
import dash_bootstrap_components as dbc

def sidebar():
    nav_links = []
    for page in dash.page_registry.values():
        if page["path"].startswith("/app2"):
            nav_links.append(
                dbc.NavLink(
                    [
                        #html.Div(page["name"], className="ms-2"),
                        html.Div('Heatmap', className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
        elif page["path"].startswith("/app3"):
                        nav_links.append(
                dbc.NavLink(
                    [
                        #html.Div(page["name"], className="ms-2"),
                        html.Div('FX Rates', className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )

        elif page["path"]=="/projects":
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div("Risk Dashboard", className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
    return dbc.Nav(children=nav_links,
                   vertical=True,
                   pills=True,
                   className="bg-primary")