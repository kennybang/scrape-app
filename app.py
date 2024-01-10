# dash_app.py
from dash import html, dcc, Dash
import plotly.express as px
import numpy as np
from scrape_standings import scrape_f1_driver_standings  # Import the function from your scraping script


years_to_scrape = list(range(2014, 2024))

# Get data from the scraping script
standings_data = scrape_f1_standings(years_to_scrape)

#Legend order
order = np.sort(standings_data["Full Name"].unique())

fig = px.line(standings_data,
                    x='Year',
                    y='Position',
                    color='Full Name',
                    title='F1 Driver Standings Over the Years',
                    markers=True,
                    category_orders={"Full Name": order},
                    hover_data=["Points"])
    
fig.update_yaxes(autorange="reversed")

# Create Dash app
app = Dash(__name__)

# Define layout
app.layout = html.Div(children=[
    html.H1("Standings Graph"),
    dcc.Graph(
        id='standings-graph',
        figure=fig,
        style={'height': '600px'} 
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
