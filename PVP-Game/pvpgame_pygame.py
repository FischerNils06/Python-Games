import pygame
from pygame.locals import * # import pygame.locals for easier access to key coordinates etc 
import sys
import random  

# Create screen
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('PVP-Game')


# Create a surface
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))


# Player 1
player_1 = pygame.Rect(0, 0, 20, 60)
player_1.center = (50, 240)
player_1_color = (0, 0, 0)
    

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    



