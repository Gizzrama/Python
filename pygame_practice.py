import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))
text = pygame.display.set_caption("Sprite")
font_size = 72
font = pygame.font.SysFont("Times New Roman", font_size)

done = False


class Sprite(pygame.sprite.Sprite()):
    def __init__ (self, width, height, colour):
        self.w = width
        self.h = height
        self.c = colour


sprite1 = Sprite(30, 30, pygame.Color("black"))
add_sprite = pygame.sprite.Group()
add_sprite.add(sprite1)
pygame.Surface(sprite1) 

