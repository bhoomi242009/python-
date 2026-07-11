import pgzrun

WIDTH = 500
HEIGHT = 500

def draw():
    screen.fill("White")

    screen.draw.filled_circle((250, 250), 100, "Yellow")
    screen.draw.circle((250, 250), 100, "Black")

    screen.draw.filled_circle((220, 220), 10, "Black")
    screen.draw.filled_circle((280, 220), 10, "Black")

    screen.draw.line((210, 290), (230, 310), "Black")
    screen.draw.line((230, 310), (250, 315), "Black")
    screen.draw.line((250, 315), (270, 310), "Black")
    screen.draw.line((270, 310), (290, 290), "Black")

pgzrun.go()
   