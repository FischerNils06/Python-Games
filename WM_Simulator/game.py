from teams import Teams
import random
import pygame

class Game:

    def __init__(self, team1, team2, draw_accepted):
        self.team1 = team1
        self.team2 = team2
        self.draw_accepted = draw_accepted

    def x_method():
        xxx = random.randint(0, 120)

        if 0 <= xxx <= 5:
            x = 0
        elif 6 <= xxx <= 15:
            x = 1
        elif 16 <= xxx <= 25:
            x = 2
        elif 26 <= xxx <= 35:
            x = 3
        elif 36 <= xxx <= 45:
            x = 4
        elif 46 <= xxx <= 55:
            x = 5
        elif 56 <= xxx <= 65:
            x = 6
        elif 66 <= xxx <= 75:
            x = 7
        elif 76 <= xxx <= 85:
            x = 8
        elif 86 <= xxx <= 90:
            x = 9
        elif 91 <= xxx <= 95:
            x = 10
        elif 96 <= xxx <= 100:
            x = 11
        elif 101 <= xxx <= 105:
            x = 12
        elif 106 <= xxx <= 110:
            x = 13
        elif 111 <= xxx <= 115:
            x = 14
        elif 116 <= xxx <= 120:
            x = 15
        return x

    def xx_method():
        xxx = random.randint(0, 50)

        if 0 <= xxx <= 5:
            x = 0
        elif 6 <= xxx <= 15:
            x = 1
        elif 16 <= xxx <= 25:
            x = 2
        elif 26 <= xxx <= 35:
            x = 3
        elif 36 <= xxx <= 45:
            x = 4
        elif 46 <= xxx <= 50:
            x = 5
        return x
       
        
    length = 45
    extra = 15
    extra_extra_lenght = xx_method()
    extra_extra_lenght2 = xx_method()
    extra_total = extra + extra_extra_lenght
    extra_total2 = extra + extra_extra_lenght2
    extra_length = x_method()
    extra_length2 = x_method()
    home_advantage = 1.05
    away_advantage = 0.95
    length_total = length + extra_length
    length_total2 = length + extra_length2
   
    def get_team1(self):
        return self.team1

    def get_team2(self):
        return self.team2

   
    def play_1_half_1(self):
        score1 = 0
        rt1 = 200 - self.team1.get_rating()
        for i in range(0, Game.length_total):
          sc1 = random.randint(0, rt1)
          if sc1 == 0 or sc1 == 1:
            score1 +=1
        return score1

    def play_1_half_2(self):
        score2 = 0
        rt2 = 200 - self.team2.get_rating()
        for i in range(0, Game.length_total):
          sc2 = random.randint(0, rt2)
          if sc2 == 0 or sc2 == 1:
            score2 +=1
        return score2

    def play_2_half_1(self):
        score3 = 0
        rt3 = 200 - self.team1.get_rating()
        for i in range(0, Game.length_total2):
          sc3 = random.randint(0, rt3)
          if sc3 == 0 or sc3 == 1:
            score3 +=1
        return score3

    def play_2_half_2(self):
        score4 = 0
        rt4 = 200 - self.team2.get_rating()
        for i in range(0, Game.length_total2):
          sc4 = random.randint(0, rt4)
          if sc4 == 0 or sc4 == 1:
            score4 +=1
        return score4
   
    
    def play_3_half_1(self):
        score5 = 0
        rt5 = 200 - self.team1.get_rating()
        for i in range(0, Game.extra_total):
          sc5 = random.randint(0, rt5)
          if sc5 == 0 or sc5 == 1:
            score5 +=1
        return score5

    def play_3_half_2(self):
        score6 = 0
        rt6 = 200 - self.team2.get_rating()
        for i in range(0, Game.extra_total):
          sc6 = random.randint(0, rt6)
          if sc6 == 0 or sc6 == 1:
            score6 +=1
        return score6

    def play_4_half_1(self):
        score7 = 0
        rt7 = 200 - self.team1.get_rating()
        for i in range(0, Game.extra_total2):
          sc7 = random.randint(0, rt7)
          if sc7 == 0 or sc7 == 1:
            score7 +=1
        return score7

    def play_4_half_2(self):
        score8 = 0
        rt8 = 200 - self.team2.get_rating()
        for i in range(0, Game.extra_total2):
          sc8 = random.randint(0, rt8)
          if sc8 == 0 or sc8 == 1:
            score8 +=1
        return score8



    