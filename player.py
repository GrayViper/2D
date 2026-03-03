import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2D interface")

clock = pygame.time.Clock()

player = pygame.Rect(380, 280, 40, 40)
speed = 5

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    screen.fill((100, 200, 100))
    pygame.draw.rect(screen, (0, 0, 255), player)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()