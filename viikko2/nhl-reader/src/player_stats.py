from player_reader import PlayerReader
from player import Player

class PlayerStats():
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = []
        for player_dict in self.players:
            if player_dict.nationality == nationality:
                players.append(player_dict)
        
        pistejärkkä = sorted(players, key=lambda player: player.total_points, reverse=True)

        return pistejärkkä