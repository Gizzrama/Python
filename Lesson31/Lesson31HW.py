#Prompt: You will create a road scene with a moving car and a traffic signal. 
#The car will travel horizontally and reverse direction whenever it reaches either side of the screen. 
#At that moment, the program will post two custom events: one changes the car colour and the other switches the traffic signal between red and green. 

import pygame
pygame.init()

background = pygame.image.load("road_traffic.jpeg")
WIDTH, HEIGHT = background.get_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Road Scene")
background = background.convert()
clock = pygame.time.Clock()

CHANGE_CAR_COLOUR = pygame.USEREVENT + 1
TOGGLE_SIGNAL = pygame.USEREVENT + 2

def RemoveWhite(surface, threshold=235):
    surface = surface.convert_alpha()
    w, h = surface.get_size()
    for x in range(w):
        for y in range(h):
            r, g, b, a = surface.get_at((x, y))
            if r > threshold and g > threshold and b > threshold:
                surface.set_at((x, y), (r, g, b, 0))
    return surface


def Recolour(surface, hue):
    out = surface.copy()
    w, h = out.get_size()
    for x in range(w):
        for y in range(h):
            r, g, b, a = out.get_at((x, y))
            if a == 0:
                continue
            c = pygame.Color(r, g, b, a)
            hh, s, v, _ = c.hsva
            if s > 50 and v > 30:         
                c.hsva = (hue, s, v, 100)
                out.set_at((x, y), c)
    return out


car_raw = RemoveWhite(pygame.image.load("car.jpeg"))
car_raw = car_raw.subsurface(car_raw.get_bounding_rect()).copy()  
scale = 130 / car_raw.get_width()
car_raw = pygame.transform.smoothscale(
    car_raw, (130, int(car_raw.get_height() * scale))
)

HUES = [0, 210, 120, 55, 280, 25]
car_variants = [Recolour(car_raw, h) for h in HUES]
colour_index = 0

car_img = car_variants[colour_index]
car_rect = car_img.get_rect(midbottom=(WIDTH // 4, HEIGHT - 12))
speed = 3
facing_right = True

LIGHT_X = 93
RED_POS, AMBER_POS, GREEN_POS = (LIGHT_X, 58), (LIGHT_X, 72), (LIGHT_X, 86)
RADIUS = 6
OFF = (35, 35, 35)
RED_ON, GREEN_ON = (235, 20, 20), (30, 220, 60)
signal_is_red = True


def DrawSignal():
    pygame.draw.circle(screen, RED_ON if signal_is_red else OFF, RED_POS, RADIUS)
    pygame.draw.circle(screen, OFF, AMBER_POS, RADIUS)
    pygame.draw.circle(screen, OFF if signal_is_red else GREEN_ON, GREEN_POS, RADIUS)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == CHANGE_CAR_COLOUR:
            colour_index = (colour_index + 1) % len(car_variants)
            car_img = car_variants[colour_index]
            if speed < 0:
                car_img = pygame.transform.flip(car_img, True, False)

        elif event.type == TOGGLE_SIGNAL:
            signal_is_red = not signal_is_red


    car_rect.x += speed


    if car_rect.right >= WIDTH or car_rect.left <= 0:
        car_rect.clamp_ip(screen.get_rect())
        speed = -speed
        car_img = pygame.transform.flip(car_img, True, False)
        pygame.event.post(pygame.event.Event(CHANGE_CAR_COLOUR))
        pygame.event.post(pygame.event.Event(TOGGLE_SIGNAL))


    screen.blit(background, (0, 0))
    DrawSignal()
    screen.blit(car_img, car_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


