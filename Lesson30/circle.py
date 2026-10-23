import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
green = (0, 255, 0)
window.fill((255, 255, 255))
pygame.draw.circle(window, green, (300, 300), 50)
pygame.draw.circle(window, green, (100, 100), 50, 3)

status = False

while not False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = True

    pygame.display.flip()

pygame.quit()