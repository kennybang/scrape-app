# dash_app.py
from dash import html, dcc, Dash, Input, Output, callback
import plotly.express as px
import numpy as np
from scrape_standings import scrape_f1_driver_standings, scrape_f1_team_standings  # Import the function from your scraping script

#Lowest is 1958
years_to_scrape = list(range(1958, 2024))

# Get data from the scraping script
driver_standings_data = scrape_f1_driver_standings(years_to_scrape)
team_standings_data = scrape_f1_team_standings(years_to_scrape)

#Dataframe for dropdown
years = team_standings_data[['Year']].copy().Year.unique()

#Legend order
driver_order = np.sort(driver_standings_data["Full Name"].unique())
team_order = np.sort(team_standings_data["Team Name"].unique())

#Start value for sliders
from_year = 2010
to_year = 2023  

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

bar_data = driver_standings_data[driver_standings_data['Year'] == 2012]

fig_bar_driver = px.bar(bar_data,
                    x='Full Name',
                    y='Points',
                    title='F1 Points for a year',
                    
                    )

print(bar_data)

fig_driver.update_yaxes(autorange="reversed")
fig_team.update_yaxes(autorange="reversed")

# Create Dash app
app = Dash(__name__)

# Define layout
app.layout = html.Div(children=[
    html.H1("Standings Graph"),

    dcc.Graph(
        id='driver_standings_graph',
        figure=fig_driver,
        style={'height': '600px'} 
    ),

    dcc.RangeSlider(years.min(), years.max(), 1, marks={years.min(): str(years.min()), years.max(): str(years.max())}, value=[from_year, to_year], tooltip={"placement": "bottom", "always_visible": True}, id='driver_slider'),

    html.Hr(),  # Horizontal line

    dcc.Graph(
        id='team_standings_graph',
        figure=fig_team,
        style={'height': '600px'} 
    ),

    dcc.RangeSlider(years.min(), years.max(), 1, marks={years.min(): str(years.min()), years.max(): str(years.max())}, value=[from_year, to_year], tooltip={"placement": "bottom", "always_visible": True}, id='team_slider'),

    html.Hr(),

        html.Div(children=[
        
        html.Div(children=[
            dcc.Graph(
            id='team_standings-graph1',
            figure=fig_team,
            style={'height': '600px', 'flex': 1} 
             ),

            dcc.RangeSlider(years.min(), years.max(), 1, marks={years.min(): str(years.min()), years.max(): str(years.max())}, value=[from_year, to_year], tooltip={"placement": "bottom", "always_visible": True}, id='some_slider'),
 
            ],
            style={'width': '50%' }
        
        ),

        html.Div(children=[
            dcc.Graph(
            id='driver_year_graph',
            figure=fig_bar_driver,
            style={'height': '600px', 'flex': 1} 
            ),
            
            dcc.Slider(years.min(), years.max(), 1, marks={years.min(): str(years.min()), years.max(): str(years.max())}, value=years.max(), tooltip={"placement": "bottom", "always_visible": True}, id="driver_year_slider" )
            
            ],

            style={'width': '50%' }
        ),
        
        
    ], style={'display': 'flex', 'flexDirection': 'row'}),
])

@callback(
    Output('driver_standings_graph', 'figure'),
    Input('driver_slider', 'value'))
def update_driver_fig(value):
    from_year, to_year = value
    filtered_data = driver_standings_data[
        (driver_standings_data['Year'] >= from_year) & (driver_standings_data['Year'] <= to_year)
    ]

    fig = px.line(
        filtered_data,
        x='Year',
        y='Position',
        color='Full Name',
        title='F1 Driver Standings Over the Years',
        markers=True,
        category_orders={"Full Name": driver_order},
        hover_data=["Points"]
    )

    fig.update_yaxes(autorange="reversed")

    fig.update_layout(transition_duration=500)

    return fig

@callback(
    Output('team_standings_graph', 'figure'),
    Input('team_slider', 'value'))
def update_team_fig(value):
    from_year, to_year = value
    filtered_data = team_standings_data[
        (team_standings_data['Year'] >= from_year) & (team_standings_data['Year'] <= to_year)
    ]

    fig = px.line(filtered_data,
                    x='Year',
                    y='Position',
                    color='Team Name',
                    title='F1 Team Standings Over the Years',
                    markers=True,
                    category_orders={"Team Name": team_order},
                    hover_data=["Points", "Name Then"])

    fig.update_yaxes(autorange="reversed")

    fig.update_layout(transition_duration=500)

    return fig

@callback(
    Output('driver_year_graph', 'figure'),
    Input('driver_year_slider', 'value'))
def update_driver_year_fig(value):

    year = value

    bar_data = driver_standings_data[driver_standings_data['Year'] == year]

    fig = px.bar(bar_data,
                x='Full Name',
                y='Points',
                title='F1 Points for a year',
                )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
