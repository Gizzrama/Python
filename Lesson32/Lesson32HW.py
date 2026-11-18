#Prompt: You will create a 500 × 400 game where a pet moves with the arrow keys to collect a food item. 
#The pet and food will be stored in a sprite group. When their Rect objects collide, the food will be removed from the group and a centered 
#"Food Collected!” message will appear over the scaled background.   

import glob
import os
import random
import sys
from collections import deque

import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Feed the Dog")
clock = pygame.time.Clock()

FOOD_NAMES = ["food", "food1", "food2", "food3", "food4"]
EXTENSIONS = (".jpeg", ".jpg", ".png")

def FindImage(name):
    for ext in EXTENSIONS:
        if os.path.exists(name + ext):
            return name + ext
    for ext in EXTENSIONS:
        matches = sorted(glob.glob(f"*_{name}{ext}"))
        if matches:
            return matches[0]
    return None


def Placeholder(size, colour):
    surf = pygame.Surface(size, pygame.SRCALPHA)
    surf.fill(colour)
    return surf


def RemoveBackground(img, tolerance = 40):
    w, h = img.get_size()
    bg = img.get_at((0, 0))
    seen = set()
    queue = deque()
    for x in range(w):
        queue.extend([(x, 0), (x, h - 1)])
    for y in range(h):
        queue.extend([(0, y), (w - 1, y)])
    while queue:
        x, y = queue.popleft()
        if (x, y) in seen or not (0 <= x < w and 0 <= y < h):
            continue
        seen.add((x, y))
        c = img.get_at((x, y))
        if (abs(c.r - bg.r) < tolerance and abs(c.g - bg.g) < tolerance
                and abs(c.b - bg.b) < tolerance):
            img.set_at((x, y), (0, 0, 0, 0))
            queue.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
    return img


def LoadSpriteImage(name, target_width, fallback_colour):
    path = FindImage(name)
    if path is None:
        print(f"[warning] could not find an image called '{name}' in {BASE_DIR}")
        return Placeholder((target_width, target_width), fallback_colour)
    try:
        img = pygame.image.load(path).convert_alpha()
        scale = target_width / img.get_width()
        img = pygame.transform.smoothscale(
            img, (target_width, int(img.get_height() * scale))
        )
        img = RemoveBackground(img)
        return img.subsurface(img.get_bounding_rect()).copy()
    except pygame.error as err:
        print(f"[warning] could not load '{path}': {err}")
        return Placeholder((target_width, target_width), fallback_colour)

def LoadBackground():
    path = FindImage("house_img")
    if path is None:
        print(f"[warning] could not find 'house_img' in {BASE_DIR}")
        return Placeholder((WIDTH, HEIGHT), (70, 90, 120))
    img = pygame.image.load(path).convert()
    return pygame.transform.smoothscale(img, (WIDTH, HEIGHT))
class Pet(pygame.sprite.Sprite):
    def __init__(self, image, pos, speed=4):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.rect.clamp_ip(screen.get_rect())


class Food(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)


background = LoadBackground()
pet = Pet(LoadSpriteImage("dog", 70, (230, 160, 60)), (60, HEIGHT - 80))
food = Food(LoadSpriteImage(random.choice(FOOD_NAMES), 50, (150, 90, 40)), (0, 0))

keep_clear = pet.rect.inflate(80, 80)
while True:
    food.rect.center = (random.randint(40, WIDTH - 40), random.randint(40, HEIGHT - 40))
    if not food.rect.colliderect(keep_clear):
        break

all_sprites = pygame.sprite.Group(pet, food)

big_font = pygame.font.SysFont(None, 56)
small_font = pygame.font.SysFont(None, 24)
message = big_font.render("Food Collected!", True, (255, 255, 255))
message_outline = big_font.render("Food Collected!", True, (0, 0, 0))
message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))   # centred on screen
hint = small_font.render("Arrow keys to move, ESC to quit", True, (255, 255, 255))

collected = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    all_sprites.update()

    if not collected and pet.rect.colliderect(food.rect):
        food.kill()
        collected = True

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    if collected:
        for dx, dy in ((-2, 0), (2, 0), (0, -2), (0, 2)):
            screen.blit(message_outline, message_rect.move(dx, dy))
        screen.blit(message, message_rect)
    else:
        screen.blit(hint, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()