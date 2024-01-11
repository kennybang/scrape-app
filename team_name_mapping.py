team_name_mapping = {
    "Mercedes": ["Mercedes GP", "Mercedes AMG Petronas Formula One Team", "Mercedes-AMG Petronas Formula One Team"],
    "Red Bull Racing": ["Red Bull Racing", "Red Bull Racing Honda", "Red Bull Racing Honda RBPT", "Red Bull Racing RBPT", "Red Bull Racing Renault", "Red Bull Racing TAG Heuer", "RBR Renault", "RBR Cosworth", "RBR Renault", "RBR Ferrari", "Red Bull Renault", "Jaguar Cosworth"],
    "Ferrari": ["Scuderia Ferrari", "Scuderia Ferrari Mission Winnow"],
    "AlphaTauri": ["AlphaTauri Honda", "AlphaTauri Honda", "AlphaTauri Honda RBPT", "AlphaTauri RBPT", "Toro Rosso", "Toro Rosso Ferrari", "STR Renault", "Scuderia Toro Rosso Honda", "STR Cosworth", "STR Ferrari", "Minardi Asiatech", "Minardi Cosworth", "Minardi Ferrari", "Minardi Ford", "Minardi Lamborghini"],
    "McLaren": ["McLaren", "McLaren Honda", "McLaren Mercedes", "McLaren Renault", "McLaren Ford", "McLaren Peugeot", "McLaren TAG", "McLaren BRM", "Mclaren BRM"],
    "Alfa Romeo": ["Alfa Romeo", "Alfa Romeo Ferrari", "Alfa Romeo Racing Ferrari", "Sauber Ferrari", "Sauber BMW", "Sauber Petronas", "Sauber Mercedes", "Sauber", "Sauber Ford"],
    "Aston Martin": ["Aston Martin", "Aston Martin Aramco Mercedes", "Aston Martin Mercedes", "Racing Point BWT Mercedes", "Force India Mercedes", "Force India Ferrari", "MF1 Toyota", "Jordan Ford", "Jordan Hart", "Jordan Honda", "Jordan Mugen Honda", "Jordan Peugeot", "Jordan Toyota", "Jordan Yamaha", "Spyker Ferrari"],
    "Lotus": ["Lotus Mercedes", "Lotus Renault", "Lotus BRM", "Lotus Climax", "Lotus Ford", "Lotus Honda", "Lotus Judd", "Lotus Lamborghini"],
    "Alpine": ["Renault", "Alpine Renault", "Benetton BMW", "Benetton Ford", "Benetton Playlife", "Benetton Renault"],
    "Williams": ["Williams", "Williams Mercedes", "Williams Renault", "Williams Cosworth", "Williams BMW", "Williams Toyota", "Williams Honda", "Williams Judd", "Williams Mecachrome", "Williams Supertec", "Williams Ford"],
    "Arrows": ["Arrows", "Arrows Asiatech", "Arrows BMW", "Arrows Cosworth", "Arrows Ford", "Arrows Megatron", "Arrows Supertec", "Arrows Yamaha", "Footwork Ford", "Footwork Hart", "Footwork Mugen Honda"],
    "Tyrell": ["Tyrrell Ford", "Tyrrell Honda", "Tyrrell Ilmor",  "Tyrrell Yamaha"],
    #"Benetton": ["Benetton BMW", "Benetton Ford", "Benetton Playlife", "Benetton Renault"], Alpine
    #"Ligier": ["Ligier Ford", "Ligier Matra", "Ligier Megatron", "Ligier Mugen Honda", "Ligier Renault"], Prost
    #"Jordan": ["Jordan Ford", "Jordan Hart", "Jordan Honda", "Jordan Mugen Honda", "Jordan Peugeot", "Jordan Toyota", "Jordan Yamaha"], Aston Martin
    "Leyton": ["Leyton House Ilmor", "Leyton House Judd"],
    "Brabham": ["Brabham Alfa Romeo", "Brabham BMW", "Brabham BRM", "Brabham Climax", "Brabham Ford", "Brabham Judd", "Brabham Repco", "Brabham Yamaha"],
    "Prost": ["Prost Acer", "Prost Mugen Honda", "Prost Peugeot", "Ligier Ford", "Ligier Matra", "Ligier Megatron", "Ligier Mugen Honda", "Ligier Renault"],
    "Marussia": ["Marussia Cosworth", "Marussia Ferrari"],
    "Dallara": ["Dallara Ferrari", "Dallara Ford", "Dallara Judd"],
    "Oselia": ["Oselia Alfa Romeo", "Oselia Ford"],
    "Larrouse": ["Larrousse Ford", "Larrousse Lamborghini", "Vanturi Lamborghini", "Lola Ford", "Lola Lamborghini"]
}   

def map_team_name(team_name):
    for preferred_name, variations in team_name_mapping.items():
        if team_name in variations:
            return preferred_name
    return team_name