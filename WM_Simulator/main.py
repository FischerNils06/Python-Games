from teams import Teams
import random
from game import Game
import pygame
from cup import Cup
from gameplay import Gameplay
from teamlist import Teamlist

if __name__ == '__main__':


    # create a game screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('World Cup Simulator')

   

    def scoreboard():
        x = 0
        y = 1
        tl = Teamlist()
        g = Gameplay(tl.teams[x], tl.teams[y])
        # draw a square at the top of the window
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,255,255), (40,40,720,100))
        pygame.display.update()
        # write the return of game_setting() to the white square
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(g.game_setting(), True, (0,0,0))
        text2 = font.render(g.game_setting_2(), True, (0,0,0))
        screen.blit(text, (50,50))
        screen.blit(text2, (50,100))
        pygame.display.update()
        
        
    scoreboard()
    running = True
    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

        

    
    
































    
    





    





   


    

