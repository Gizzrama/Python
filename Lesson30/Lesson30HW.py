#You will create a simple Pygame screen where a rectangle sprite can move using the arrow keys. 
#The program will draw both solid and outlined circles, keep the sprite inside the screen using boundaries, 
#and change the sprite color when it touches the left, right, top, or bottom edge.

import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
caption = pygame.display.set_caption("Colour changing sprite")
blue = (0, 0, 255)
screen.fill((255, 255, 255))
pygame.draw.circle(screen, blue, (300, 300), 50)
pygame.draw.circle(screen, blue, (100, 100), 50, 2)

colours = {
        "red": pygame.Color("red"),
        "blue":pygame.Color("blue"),
        "green":pygame.Color("green"),
        "yellow":pygame.Color("yellow"),
        "black":pygame.Color("black")
    }

current_colour = colours["red"]
x, y = 220, 220
sprite_width, sprite_height = 60, 60
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= 4
    if pressed[pygame.K_RIGHT]:
        x += 4
    if pressed[pygame.K_UP]:
        y -= 4
    if pressed[pygame.K_DOWN]:
        y += 4

    x = min(max(0, x), 500 - sprite_width)
    y = min(max(0, y), 500 - sprite_height)

    if x == 0:
        current_colour = colours["blue"]
    elif x == 500 - sprite_width:
        current_colour = colours["yellow"]
    elif y == 0:
        current_colour = colours["red"]
    elif y == 500 - sprite_height:
        current_colour = colours["green"]
    else:
        current_colour = colours["black"]

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, blue, (400, 400), 50)
    pygame.draw.circle(screen, blue, (100, 100), 50, 2)
    pygame.draw.rect(screen, current_colour, (x, y, sprite_width, sprite_height))

    pygame.display.flip()
    clock.tick(1000)

pygame.quit()