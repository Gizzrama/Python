import pygame
import math
import random

screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27

def score(x, y):
    display = font.render("score:" + str(score_value), True, (255, 255, 255))
    screen.blit(display, (x, y))

def game_over_text():
    display = over_font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(display, (200, 250))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    return distance 



pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

backgroud = pygame.image.load("background.png")
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

player_img = pygame.image.load("player.png")
player_x = player_start_x
player_y = player_start_y
player_x_change = 0

enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_num = 6

for i in enemy_num:
    enemy_img.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0, screen_width - 64))
    enemy_y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = player_start_y
bullet_x_change = bullet_speed_y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10
over_font = pygame.font.Font("freesansbold.ttf", 64)


