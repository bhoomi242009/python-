import pygame
from pygame.locals import *
from time import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
rocketx = 350
rockety = 400
rocket = pygame.image.load("images/rocket.png") #rocket loading onto the screen
background = pygame.image.load("images/background_space.png")
keys = [False, False, False, False] #up, left, down, right
#Right now all keys are false, but will be true when key is pressed

while rockety < 600:
    screen.blit(background, (0, 0))
    screen.blit(rocket, (rocketx, rockety))
    pygame.display.flip()
    for event in pygame.event.get():
        #its to stop the game when i press the cross sign
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0) #exiting all the libraries/loaded from the system

        #to check if any eyboard or key was pressed/released
        if event.type == pygame.KEYDOWN:
            #check which button is pressed
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            if event.key == K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:
            #check which button is released
            if event.key == K_UP:
                keys[0] = False
            elif event.key == K_LEFT:
                keys[1] = False
            elif event.key == K_DOWN:
                keys[2] = False
            if event.key == K_RIGHT:
                keys[3] = False
            
        #based on which key is true/ false, we decide how much it will move
    if keys[0]:
        if rockety > 0:
            rockety -= 5 #rockety = rockety - 5
    elif keys[1]:
        if rocketx > 0:
            rocketx -= 5
    elif keys[2]:
        if rockety < 550:
            rockety += 5
    elif keys[3]:
        if rocketx < 750:
            rocketx += 5

        #rockety += 5
    sleep(0.05)
    print("Game over")