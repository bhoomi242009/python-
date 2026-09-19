import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

screen.fill(white)

class Circle():
    def __init__(self, color, pos, rad, wid = 0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.wid = wid
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self. color, self.pos, self.rad, self.wid)

    def grow(self, x):
        self.rad += x
        pygame.draw.circle(self.screen, self. color, self.pos, self.rad, self.wid) 

position = (300, 300)
radius = 50
wid = 2

pygame.draw.circle(screen, red, position, radius, wid)
pygame.display.update()

redcircle = Circle(red, position, radius + 60)
greencircle = Circle(green, position, radius+40)
yellowcircle = Circle(yellow, position, radius, 5)
bluecircle = Circle(blue, position, 20)

while True:
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            redcircle.draw()
            greencircle.draw()
            yellowcircle.draw()
            bluecircle.draw()
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            bluecircle.grow(2)
            greencircle.grow(2)
            redcircle.grow(2)
            yellowcircle.grow(2)
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            blackcircle = Circle(black, pos, 1)
            blackcircle.draw()
            pygame.display.update()

pygame.quit()
