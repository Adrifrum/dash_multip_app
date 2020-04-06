import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from navbar import Navbar

#Modifications hufhufh


nav = Navbar()


body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.H2("Manon SARDEING-FRUMENCE, Avocate Penaliste"),
                     html.P(
                         """\
Depuis sa création, le cabinet d'avocats pénalistes SARDEING-FRUMENCE se consacre exclusivement à la défense de personnes physiques ou morales confrontées à une procédure pénale en qualité de mises en cause ou de victimes.

Ayant fait le choix d’une spécialisation unique, nos avocats pénalistes ont acquis au fil des années une solide expérience de la défense pénale en intervenant sur les affaires les plus complexes dans des environnements parfois difficiles.

Chaque avocat pénaliste du cabinet est ainsi amené à intervenir régulièrement auprès des services d’enquête et des juridictions spécialisées dans les domaines les plus techniques du droit pénal."""
                           ),
                           dbc.Button("Plus de details", color="secondary"),
                   ],
                  md=4,
               ),
              dbc.Col(
                 [
                     html.H2("Taux d'acquittement du cabinet:"),
                     dcc.Graph(
                         figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                            ),
                        ]
                     ),
                ]
            )
       ],
className="mt-4",
)

def Homepage():
    layout = html.Div([
    nav,
    body
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SKETCHY])
app.layout = Homepage()
if __name__ == "__main__":
    app.run_server()
