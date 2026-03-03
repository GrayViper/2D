
import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Style Game")

clock = pygame.time.Clock()

MAP_WIDTH = 800
MAP_HEIGHT = 600

player = pygame.Rect(100, 100, 40, 40)
speed = 5

# 🌿 Grass area
grass = pygame.Rect(300, 200, 200, 150)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    old_x = player.x
    old_y = player.y

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Border collision
    if player.left < 0 or player.right > MAP_WIDTH:
        player.x = old_x

    if player.top < 0 or player.bottom > MAP_HEIGHT:
        player.y = old_y

    # 🌿 Check grass collision
    if player.colliderect(grass):
        if random.randint(1, 150) == 1:
            print("🌟 A wild Pokémon appeared!")

    # Draw background
    screen.fill((100, 200, 100))

    # Draw border
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, MAP_WIDTH, MAP_HEIGHT), 5)

    # Draw grass
    pygame.draw.rect(screen, (0, 150, 0), grass)

    # Draw player
    pygame.draw.rect(screen, (0, 0, 255), player)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()