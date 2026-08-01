import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

diver = Actor("diverr")
diver.pos = 100, 100

pearl = Actor("pearl")
pearl.pos = 200, 200


def draw():
    screen.blit("background ocean", (0, 0))
    pearl.draw()
    diver.draw()

    screen.draw.text("Score: " + str(score), color="white", topleft=(10, 10))

    if game_over:
        screen.fill("darkblue")
        screen.draw.text(
            "Time's up! Final score: " + str(score),
            midtop=(WIDTH / 2, 10),
            fontsize=40,
            color="white"
        )


def place_pearl():
    pearl.x = randint(70, WIDTH - 70)
    pearl.y = randint(70, HEIGHT - 70)


def time_up():
    global game_over
    game_over = True


def update():
    global score

    if keyboard.left:
        diver.x = diver.x - 2

    if keyboard.right:
        diver.x = diver.x + 2

    if keyboard.up:
        diver.y = diver.y - 2

    if keyboard.down:
        diver.y = diver.y + 2

    pearl_collected = diver.colliderect(pearl)

    if pearl_collected:
        score = score + 10
        place_pearl()


clock.schedule(time_up, 60.0)

pgzrun.go()