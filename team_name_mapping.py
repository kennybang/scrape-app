team_name_mapping = {
    "Mercedes": ["Mercedes GP", "Mercedes AMG Petronas Formula One Team", "Mercedes-AMG Petronas Formula One Team"],
    "Red Bull Racing": ["Red Bull Racing", "Red Bull Racing Honda", "Red Bull Racing Honda RBPT", "Red Bull Racing RBPT", "Red Bull Racing Renault", "Red Bull Racing TAG Heuer"],
    "Ferrari": ["Scuderia Ferrari", "Scuderia Ferrari Mission Winnow"],
    "AlphaTauri": ["AlphaTauri Honda", "AlphaTauri Honda", "AlphaTauri Honda RBPT", "AlphaTauri RBPT", "Toro Rosso", "Toro Rosso Ferrari", "STR Renault", "Scuderia Toro Rosso Honda"],
    "McLaren": ["McLaren", "McLaren Honda", "McLaren Mercedes", "McLaren Renault"],
    "Alfa Romeo": ["Alfa Romeo", "Alfa Romeo Ferrari", "Alfa Romeo Racing Ferrari", "Sauber Ferrari"],
    "Aston Martin": ["Aston Martin", "Aston Martin Aramco Mercedes", "Aston Martin Mercedes", "Racing Point BWT Mercedes", "Force India Mercedes"],
    "Lotus": ["Lotus Mercedes", "Lotus Renault"],
    "Alpine": ["Renault", "Alpine Renault"]
}   

def map_team_name(team_name):
    for preferred_name, variations in team_name_mapping.items():
        if team_name in variations:
            return preferred_name
    return team_name