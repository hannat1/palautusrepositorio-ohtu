class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.total_points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} team {self.team} goals {self.goals:3} assists {self.assists} total = {self.total_points}"
