# dash_app.py
from dash import html, dcc, Dash
import plotly.express as px
import numpy as np
from scrape_standings import scrape_f1_driver_standings, scrape_f1_team_standings  # Import the function from your scraping script


years_to_scrape = list(range(2014, 2024))

# Get data from the scraping script
driver_standings_data = scrape_f1_driver_standings(years_to_scrape)
team_standings_data = scrape_f1_team_standings(years_to_scrape)

#Legend order
driver_order = np.sort(driver_standings_data["Full Name"].unique())
team_order = np.sort(team_standings_data["Team Name"].unique())

fig_driver = px.line(driver_standings_data,
                    x='Year',
                    y='Position',
                    color='Full Name',
                    title='F1 Driver Standings Over the Years',
                    markers=True,
                    category_orders={"Full Name": driver_order},
                    hover_data=["Points"])

fig_team = px.line(team_standings_data,
                    x='Year',
                    y='Position',
                    color='Team Name',
                    title='F1 Team Standings Over the Years',
                    markers=True,
                    category_orders={"Team Name": team_order},
                    hover_data=["Points", "Name Then"])
    
fig_driver.update_yaxes(autorange="reversed")
fig_team.update_yaxes(autorange="reversed")

# Create Dash app
app = Dash(__name__)

# Define layout
app.layout = html.Div(children=[
    html.H1("Standings Graph"),
    dcc.Graph(
        id='driver_standings-graph',
        figure=fig_driver,
        style={'height': '600px'} 
    ),
    dcc.Graph(
        id='team_standings-graph',
        figure=fig_team,
        style={'height': '600px'} 
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
