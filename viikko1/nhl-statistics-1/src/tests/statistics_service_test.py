import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_konstruktori_luo_pelaajat(self):
        self.assertAlmostEqual(len(self.stats._players), 5)

    def test_team(self):
        team = self.stats.team("EDM")
        team_test = ["Semenko", "Kurri", "Gretzky"]
        self.assertEqual([player.name for player in team], team_test)

    def test_search_match(self):
        self.assertAlmostEqual(str(self.stats.search("Yzerman")), "Yzerman DET 42 + 56 = 98")

    def test_search_no_match(self):
        self.assertAlmostEqual(self.stats.search("Erik"), None)

    def test_top_2(self):
        top2 = self.stats.top(1)
        top2_test = ["Gretzky", "Lemieux"]
        self.assertEqual([player.name for player in top2], top2_test)

    def test_method_goals(self):
        top_goals = self.stats.top(1, SortBy.GOALS)
        top_goals_test = ["Lemieux", "Yzerman"]
        self.assertEqual([player.name for player in top_goals], top_goals_test)

    def test_method_assists(self):
        top_assists = self.stats.top(1, SortBy.ASSISTS)
        top_assists_test = ["Gretzky", "Yzerman"]
        self.assertEqual([player.name for player in top_assists], top_assists_test)