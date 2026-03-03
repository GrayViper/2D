import pygame
import sys

pygame.init()

# Create window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pokemon Style Game")

clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100, 200, 100))  # green background

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()