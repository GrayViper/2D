import pygame
import sys
import random

pygame.init()

# Screen setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Style Game")

clock = pygame.time.Clock()

# Map size
MAP_WIDTH = 800
MAP_HEIGHT = 600

# Player
player = pygame.Rect(100, 100, 40, 40)

# Grass area
grass = pygame.Rect(300, 200, 200, 150)

# Trees (obstacles)
trees = [
    pygame.Rect(200, 150, 60, 60),
    pygame.Rect(450, 350, 60, 60),
    pygame.Rect(600, 100, 60, 60),
    pygame.Rect(150, 400, 60, 60)
]

# NPC
npc = pygame.Rect(650, 450, 40, 40)

# Text system
font = pygame.font.SysFont(None, 28)
message = ""

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Interaction with NPC
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if player.colliderect(npc):
                    message = "Hello trainer! Welcome to DevMon!"

    keys = pygame.key.get_pressed()

    # Save old position
    old_x = player.x
    old_y = player.y

    # Default speed
    speed = 5

    # Slower movement in grass
    if player.colliderect(grass):
        speed = 3

    # Movement
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

    # Tree collision
    for tree in trees:
        if player.colliderect(tree):
            player.x = old_x
            player.y = old_y

    # Remove dialogue if player walks away from NPC
    if not player.colliderect(npc):
        message = ""

    # Random encounter in grass
    if player.colliderect(grass):
        if random.randint(1, 150) == 1:
            print("🌟 A wild Pokémon appeared!")

    # Drawing
    screen.fill((100, 200, 100))

    # Map border
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, MAP_WIDTH, MAP_HEIGHT), 5)

    # Grass
    pygame.draw.rect(screen, (0, 150, 0), grass)

    # Trees
    for tree in trees:
        pygame.draw.rect(screen, (34, 139, 34), tree)

    # NPC
    pygame.draw.rect(screen, (255, 200, 0), npc)

    # Player
    pygame.draw.rect(screen, (0, 0, 255), player)

    # Dialogue text
    if message:
        text = font.render(message, True, (0, 0, 0))
        screen.blit(text, (20, 560))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()