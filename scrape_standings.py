import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
import numpy as np
from team_name_mapping import map_team_name

def scrape_f1_driver_standings(years):
    # Create an empty DataFrame to store the data
    columns = ['Position', 'Name', 'Surname', 'Full Name', 'Points', 'Year']
    all_data = pd.DataFrame(columns=columns)

    for year in years:
        url = f"https://www.formula1.com/en/results.html/{year}/drivers.html"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the table body with standings data
            table_body = soup.find('tbody')

            if table_body:
                # Extract data from each row
                rows = table_body.find_all('tr')
                data = []

                for row in rows:

                    # Extract data from individual elements in the row
                    name_element = row.find('span', class_='hide-for-tablet')
                    surname_element = row.find('span', class_='hide-for-mobile')
                    position_element = row.find('td', class_='dark')
                    points_element = row.find('td', class_='dark bold')

                    # Extract text content from elements
                    name = name_element.text if name_element else None
                    surname = surname_element.text if surname_element else None
                    position = position_element.text if position_element else None
                    points = points_element.text if points_element else None

                    

                    # Append data to the list
                    if position != "DQ":    #Avoid Schumachers DQ :sadface:
                        data.append([int(position), name, surname,  f"{name} {surname}", float(points), int(year)])

                # Create a DataFrame using the collected data
                df = pd.DataFrame(data, columns=columns)

                # Append the DataFrame for the current year to the overall DataFrame
                all_data = pd.concat([all_data, df], ignore_index=True)

            else:
                print(f"Table body not found for year {year}.")

        else:
            print(f"Failed to retrieve data for year {year}. Status Code: {response.status_code}")

    #print(all_data) #For debugging
    return all_data

def scrape_f1_team_standings(years):
    # Create an empty DataFrame to store the data
    columns = ['Position', 'Team Name', 'Name Then', 'Points', 'Year']
    all_data = pd.DataFrame(columns=columns)

    for year in years:
        url = f"https://www.formula1.com/en/results.html/{year}/team.html"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the table body with standings data
            table_body = soup.find('tbody')

            if table_body:
                # Extract data from each row
                rows = table_body.find_all('tr')
                data = []

                for row in rows:

                    # Extract data from individual elements in the row
                    team_name_element = row.find('a', class_='dark bold uppercase ArchiveLink')
                    position_element = row.find('td', class_='dark')
                    points_element = row.find('td', class_='dark bold')

                    # Extract text content from elements
                    team_name = team_name_element.text if team_name_element else None
                    position = position_element.text if position_element else None
                    points = points_element.text if points_element else None

                    curr_name = map_team_name(team_name)

                    # Append data to the list
                    if position != "EX":    #Avoid Schumachers DQ :sadface:
                        data.append([int(position), curr_name, team_name,  points, int(year)])

                # Create a DataFrame using the collected data
                df = pd.DataFrame(data, columns=columns)

                # Append the DataFrame for the current year to the overall DataFrame
                all_data = pd.concat([all_data, df], ignore_index=True)

            else:
                print(f"Table body not found for year {year}.")

        else:
            print(f"Failed to retrieve data for year {year}. Status Code: {response.status_code}")

    #print(all_data) #For debugging
    return all_data



if __name__ == "__main__":
    # Years to scrape
    years_to_scrape = list(range(2014, 2024))
    all_standings_data = scrape_f1_team_standings(years_to_scrape)
    
    """
    #Legend order
    order = np.sort(all_standings_data["Full Name"].unique())

    fig = px.line(all_standings_data,
                    x='Year',
                    y='Position',
                    color='Full Name',
                    title='F1 Standings Over the Years',
                    markers=True,
                    category_orders={"Full Name": order},
                    hover_data=["Points"])
    
    fig.update_yaxes(autorange="reversed")

    fig.show()

    """


