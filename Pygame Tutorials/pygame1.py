import pygame
import sys

#Set up the screen
pygame.init()
screen = pygame.display.set_mode((1200, 595))
pygame.display.set_caption("Tutorial 1")
clock = pygame.time.Clock()

def draw():
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,0), (x,y,width,height))
    pygame.display.update()



x = 300
y = 300
speed = 3
width = 40
height = 80
# create two walls at the left and right side of the screen
linkewand = pygame.Rect(0,0,1,600)
rechtewand = pygame.Rect(1199,0,1,600)
# create a floor at the bottom of the screen

#color of floor is green

boden = pygame.draw.rect(screen, (0,255,0), (0,580,1200,1))

def floor():
    pygame.draw.rect(screen, (0,255,0), (0,580,1200,99))
    pygame.display.update()
    





# Main game loop
go = True

while go:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            sys.exit() # Flag that we are done so we exit this loop

    rect = pygame.Rect(x ,y ,40,80)
    gedrueckt = pygame.key.get_pressed()
    if gedrueckt[pygame.K_UP]:
        
        y -= speed # x geht nach oben bei minus

    if gedrueckt[pygame.K_LEFT] and not rect.colliderect(linkewand):
        x -= speed

    if gedrueckt[pygame.K_RIGHT] and not rect.colliderect(rechtewand):
        x += speed

    if gedrueckt[pygame.K_DOWN] and not rect.colliderect(boden):
        y += speed


    #make it faster when you hold down the key
    if gedrueckt[pygame.K_k]:
        speed = 5
    else:
        speed = 3

    
    draw()
    floor()
    
    clock.tick(60)