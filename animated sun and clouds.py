import pgzrun 

WIDTH = 800
HEIGHT = 600

sun_x = 50
sun_y = 100

def draw():
    screen.fill((135, 206, 235))
    screen.draw.filled_circle((sun_x, sun_y), 40, "Yellow")

    screen.draw.filled_circle((150, 120), 30, "White")
    screen.draw.filled_circle((180, 100), 35, "White")
    screen.draw.filled_circle((210, 120), 30, "White")

    screen.draw.filled_circle((500, 150), 30, "White")
    screen.draw.filled_circle((530, 130), 35, "White")
    screen.draw.filled_circle((560, 150), 30, "White")

    screen.draw.filled_rect(Rect((0, 500),(800, 100)), "Green")

def update():
    global sun_x

    sun_x += 0.5

    if sun_x > WIDTH + 40:
        sun_x = -40

pgzrun.go()


