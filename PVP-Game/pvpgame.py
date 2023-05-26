import pygame
import sys
import random
import time


pygame.init()

clock = pygame.time.Clock()

# Set up the window
WINDOWWIDTH = 1000
WINDOWHEIGHT = 500

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('PvP Game')

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set the Background Color of the window
windowSurface.fill(WHITE)

# Squares for the players
# Red Square
player1 = pygame.Rect(950, 400, 30, 30)

# Blue Square
player2 = pygame.Rect(20, 400, 30, 30)

# Floor
floor = pygame.Rect(0, 430, 1000, 30)

# Squares for the walls
# Left wall
leftWall = pygame.Rect(15, 0, 5, 500)
# Right wall
rightWall = pygame.Rect(980, 0, 5, 500)


# Set the initial vertical speed of the players to 0
player1_speedy = 0
player2_speedy = 0

# Set the vertical acceleration of the players
GRAVITY = 0.5

# Set the score of the players to 0
score_player1 = 0
score_player2 = 0

# Set up the font for the scoreboard
score_font = pygame.font.Font(None, 60)

# Main game loop
while True:
    QUIT = pygame.QUIT
    # Check if the user wants to quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

     # Calculate the elapsed time since the last frame in seconds
    dt = clock.tick(60) / 1000.0

    # Move the players
    speed = 200 * dt

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT] and not player1.colliderect(leftWall):
        pygame.draw.rect(windowSurface, WHITE, player1)
        player1.x -= speed 
    if pressed[pygame.K_RIGHT] and not player1.colliderect(rightWall):
        pygame.draw.rect(windowSurface, WHITE, player1)
        player1.x += speed


    if pressed[pygame.K_a] and not player2.colliderect(leftWall):
        pygame.draw.rect(windowSurface, WHITE, player2)
        player2.x -= speed
    if pressed[pygame.K_d] and not player2.colliderect(rightWall):
        pygame.draw.rect(windowSurface, WHITE, player2)
        player2.x += speed

    


    # Check if player1 is on top of player2
    if player1.bottom == player2.top and player1.left <= player2.left <= player1.right or player1.bottom == player2.top and player1.left <= player2.right <= player1.right: 
        pygame.draw.rect(windowSurface, WHITE, player2)
        player2.x = 20
        player2.y = 400
        pygame.draw.rect(windowSurface, WHITE, player1)
        score_player1 += 1
        
    # Check if player2 is on top of player1
    if player2.bottom == player1.top and player1.left <= player2.right <= player1.right or player2.bottom == player1.top and player1.left <= player2.left <= player1.right: 
        pygame.draw.rect(windowSurface, WHITE, player1)
        player1.x = 950
        player1.y = 400
        pygame.draw.rect(windowSurface, WHITE, player2)
        score_player2 += 1
        


    # Jump if the up arrow or the w key is pressed
    if pressed[pygame.K_UP] and player1.bottom == floor.top:
        pygame.draw.rect(windowSurface, WHITE, player1)
        player1_speedy = -6
    if pressed[pygame.K_w] and player2.bottom == floor.top:
        pygame.draw.rect(windowSurface, WHITE, player2)
        player2_speedy = -6

    # Update the vertical speed of the players based on gravity
    player1_speedy += GRAVITY
    player2_speedy += GRAVITY

    # Update the vertical position of the players
    pygame.draw.rect(windowSurface, WHITE, player1)
    player1.y += player1_speedy
    pygame.draw.rect(windowSurface, WHITE, player2)
    player2.y += player2_speedy

    # Make sure the players stay above the floor
    if player1.bottom > floor.top:
        player1.bottom = floor.top
        player1_speedy = 0
    if player2.bottom > floor.top:
        player2.bottom = floor.top
       

   
    # Draw the player1
    pygame.draw.rect(windowSurface, RED, player1)

    # Draw the player2
    pygame.draw.rect(windowSurface, BLUE, player2)

    # Draw the floor
    pygame.draw.rect(windowSurface, BLACK, floor)

    # Draw the walls
    pygame.draw.rect(windowSurface, BLACK, leftWall)
    pygame.draw.rect(windowSurface, BLACK, rightWall)

    # Update the scores
    # delete the previous score
 
    score_text1 = score_font.render('RED ' + str(score_player1) + ' : ' + str(score_player2) + ' BLUE' , True, BLACK)
    score_text_rect1 = score_text1.get_rect()
    score_text_rect1.centerx = windowSurface.get_rect().centerx
    windowSurface.blit(score_text1, score_text_rect1)
    pygame.draw.rect(windowSurface, WHITE, score_text_rect1)
    score_text1 = score_font.render('RED ' + str(score_player1) + ' : ' + str(score_player2) + ' BLUE' , True, BLACK)
    score_text_rect1 = score_text1.get_rect()
    score_text_rect1.centerx = windowSurface.get_rect().centerx
    windowSurface.blit(score_text1, score_text_rect1)


    
  

    # Update the display
    pygame.display.update()
