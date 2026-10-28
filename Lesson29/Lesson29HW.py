#Prompt: You will create a 500 × 500 wildlife display featuring a tiger image over a background. 
#The screen will show the heading “Wildlife Spotlight: Tiger” and a short tiger fact. 
#The program will repeatedly draw the images and text until the user closes the window,
#while a Clock object keeps the application running at 30 frames per second.

import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
background_image = pygame.transform.scale(pygame.image.load("white_background.jpg").convert() (500, 500))
tiger = pygame.image.load("tiger.jPeg").convert_alpha(), (200, 200)
tiger_rect = tiger.get_rect(center=(500 // 2, 500 // 2 - 30))
fact = pygame.font.Font(None, 40).render("Wildlife Spotlight: Tiger - Tigers are the largest wild cats in the world", True, pygame.color("black"))
fact_rect = fact.get_rect(center=(500 // 2, 500 // 2 + 110)) 

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))
        screen.blit(tiger, tiger_rect)
        screen.blit(fact, fact_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()