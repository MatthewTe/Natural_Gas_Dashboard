import dash
import dash_core_components as dcc
import dash_html_components as html
from Database_return import gas_prices


# Deffining the Application:
app = dash.Dash()

# Describing the app layout:
app.layout = html.Div(children=[

# Creating a dash_core_components graph object as a child:
    dcc.Graph(
        id = "Natural Gas Prices",
        figure = {
            'data' : [
            {'x': gas_prices().index, 'y': gas_prices(),'type': 'line', 'name': 'Nat Gas'}],
            'layout' : {
                'title': "Natural Gas Price"
                }
            }
        )
    ]
)
# Running the dashboard server:
def dashboard_run(Bool):
    if Bool == True:
        if __name__ =='__main__':
            app.run_server(debug=True)
    else:
        pass

dashboard_run(False)
