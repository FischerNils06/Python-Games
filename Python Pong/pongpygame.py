import pygame


#Set up the screen
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pong")

#Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Draw the screen
screen.fill(BLACK)
pygame.draw.line(screen, WHITE, [320, 0], [320, 480], 2)
pygame.draw.line(screen, WHITE, [0, 240], [640, 240], 2)

#Draw the paddles
paddle_a = pygame.draw.line(screen, WHITE, [10, 200], [10, 280], 10)
paddle_b = pygame.draw.line(screen, WHITE, [630, 200], [630, 280], 10)

#Draw the ball
pygame.draw.circle(screen, WHITE, [320, 240], 10, 0)

#Update the screen
pygame.display.flip()

# Methods




# Keyboard bindings
keys=pygame.key.get_pressed()
if keys[pygame.K_w]:
    paddle_a_up()
if keys[pygame.K_s]:
    paddle_a_down()
if keys[pygame.K_UP]:
    paddle_b_up()
if keys[pygame.K_DOWN]:
    paddle_b_down()



#Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False









    