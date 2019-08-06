import dash
import dash_core_components as dcc
import dash_html_components as html

# Deffining the Application:
app = dash.Dash()

# Describing the app layout:
app.layout = html.Div(childern=[

])
# Running the dashboard server:
def dashboard_run(Bool):
    if Bool == True:
        if __name__ =='__main__':
            app.run_server(debug=True)
    else:
        pass

dashboard_run(False)
