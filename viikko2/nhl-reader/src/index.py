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

    pistejärkkä = sorted(players, key=lambda player: player.total_points, reverse=True)

    print("Players from FIN:")

    for player in pistejärkkä:
        print(player)

if __name__ == "__main__":
    main()
