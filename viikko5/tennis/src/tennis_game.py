DICT = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty", 4: "Deuce"}


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score1 += 1
        else:
            self.score2 += 1

    def even(self, score1):
        score = ""
        if score1 >= 3:
            return "Deuce"
        score = DICT[score1] + "-All"
        return score

    def winning(self, score1, score2):
        whos_winning = score1 - score2

        if whos_winning == 1:
            score = "Advantage " + self.player1_name
        elif whos_winning == -1:
            score = "Advantage " + self.player2_name
        elif whos_winning >= 2:
            score = "Win for " + self.player1_name
        else:
            score = "Win for " + self.player2_name
        return score

    def middle_game(self, score1, score2):
        score = ""
        temp_score = 0
        for i in (score1, score2):
            score += DICT[i]
            if temp_score == 0:
                score += "-"
                temp_score += 1
        return score

    def get_score(self):
        if self.score1 == self.score2:
            return self.even(self.score1)

        elif self.score1 >= 4 or self.score2 >= 4:
            return self.winning(self.score1, self.score2)

        else:
            return self.middle_game(self.score1, self.score2)
