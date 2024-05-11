import pygame
import sys
from random import randint, choice

# Pygame-ის ინიციალიზაცია
pygame.init()

# ფანჯრის არეალის დაყენება
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

GREEN = (50, 209, 93)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Test Pygame")


class Enemy:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = randint(0, WINDOW_WIDTH - self.width)
        self.y = randint(0, WINDOW_HEIGHT - self.height)
        self.color = choice([YELLOW, BLUE])
        self.speed = choice([2, 3, 4])

    def move(self):
        self.x += self.speed
        if self.x > WINDOW_WIDTH:
            self.x = -self.width
            self.y = randint(0, WINDOW_HEIGHT - self.height)

    def draw(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

# მტრების შექმნა
enemies = [Enemy() for _ in range(5)]

# მოთამაშის აღწერა
player_width = 50
player_height = 50
player_x = 250
player_y = 350
player_speed = 5

# თამაშის ციკლი
running = True
while running:
    window.fill(GREEN) # ფანჯრის შევსება მწვანე ფერით

    # მოვლენების დამუშავება
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ყველა კლავიატურის კლავიშის მდგომარეობის მიღება
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < WINDOW_HEIGHT - player_height:
        player_y += player_speed

    # მტრების გამოჩენა ეკრანზე
    for enemy in enemies:
        enemy.move()
        enemy.draw()

    # მოთამაშის გამოჩენა ეკრანზე
    pygame.draw.rect(window, RED, (player_x, player_y, player_width, player_height))

    # ეკრანის გნახლება
    pygame.display.update()

    # კადრები სიჩქარის შეზღუდვა
    pygame.time.Clock().tick(240)

pygame.quit()
sys.exit()
