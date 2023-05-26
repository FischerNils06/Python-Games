from teams import Teams
from game import Game
import random

class Gameplay:

    def __init__(self, x, y):
        self._x = x
        self._y = y


    def game_setting(self):
        return f"{self._x.get_name()} vs {self._y.get_name()}"

    def game_setting_2(self):
        g1 = Game(self._x, self._y, True)
        s11 = g1.play_1_half_1()
        s12 = g1.play_1_half_2()
        s21 = g1.play_2_half_1()
        s22 = g1.play_2_half_2()

        score_team1_1 = s11
        score_team2_1 = s12
        score_team1 = s11 + s21
        score_team2 = s12 + s22

        return f"{score_team1_1} : {score_team2_1}  |  {score_team1} : {score_team2}"