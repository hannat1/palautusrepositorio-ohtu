<<<<<<< HEAD
import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()
    players = []
    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == 'FIN':
            players.append(player)
    print("Players from FIN:")

    for player in players:
        print(player)
=======
from rich.console import Console
from rich.table import Table
from player_stats import PlayerStats
from player_reader import PlayerReader

def main():
    console = Console()
    while True:

        season = input("Select season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25]:")
        nationality = input("Select nationality [AUS/CZE/AUT/GER/DEN/SUI/CAN/LAT/BLR/SLO/GBR/FIN/SWE/RUS/NOR]:")

        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers of {nationality} season {season}")
        table.add_column("name", style="cyan")
        table.add_column("team", style="bold magenta")
        table.add_column("goals", justify="right", style="bold green")
        table.add_column("assists", justify="right", style="bold green")
        table.add_column("points", justify="right", style="bold green")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.total_points))
        console.print(table)
>>>>>>> main

if __name__ == "__main__":
    main()
