import pgzrun
import pygame
from random import randint

WIDTH = 800
HEIGHT = 600

ship = pygame.image.load("ship.jpg")
player = pygame.image.load("seashell.jpg")

ship = pygame.transform.scale(ship, (70, 70))
player = pygame.transform.scale(player, (50, 50))

ship_x = 400
ship_y = 300

players = []

for i in range(5):
    players.append([randint(50, 750), randint(100, 550)])

score = 0

def draw():
    screen.clear()
    screen.fill("black")
    screen.blit(ship, (ship_x, ship_y))

    for x, y in players:
        screen.surface.blit(player, (x, y))

    screen.draw.text("Score: " + str(score), (20, 20), fontsize = 40, color = "white")

def update():
    global ship_x, ship_y, score

    if keyboard.left:
        ship_x = ship_x - 5
    if keyboard.right:
        ship_x = ship_x + 5
    if keyboard.up:
        ship_y = ship_y - 5
    if keyboard.down:
        ship_y = ship_y + 5

    ship_x = max(0, min(WIDTH - 70, ship_x))
    ship_y = max(0, min(HEIGHT - 70, ship_y))

    ship_rect = pygame.Rect(ship_x, ship_y, 70, 70)

    for player in players:
        player_rect = pygame.Rect(player[0], player[1], 50, 50)

        if ship_rect.colliderect(player_rect):
            score = score + 1
            player[0] =  randint(50, 750)
            player[1] = randint(100, 550)

def move_players():
    for player in players:
        player[0] =  randint(50, 750)
        player[1] = randint(100, 550)

clock.schedule_interval(move_players, 2)

pgzrun.go()
