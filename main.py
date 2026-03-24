import pygame
import sys
import random
import os

pygame.init()

# Screen setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Style Game")

clock = pygame.time.Clock()

# Load images (using your "assessts" folder)
player_img = pygame.image.load(os.path.join("assessts","player.png")).convert_alpha()
tree_img = pygame.image.load(os.path.join("assessts","tree.png")).convert_alpha()
grass_img = pygame.image.load(os.path.join("assessts","grass.png")).convert_alpha()
npc_img = pygame.image.load(os.path.join("assessts","npc.png")).convert_alpha()

# Resize
player_img = pygame.transform.scale(player_img,(40,40))
tree_img = pygame.transform.scale(tree_img,(60,60))
grass_img = pygame.transform.scale(grass_img,(200,150))
npc_img = pygame.transform.scale(npc_img,(40,40))

# Map
MAP_WIDTH = 800
MAP_HEIGHT = 600

# Player
player = pygame.Rect(100,100,40,40)

# Bounce animation
bob_offset = 0
bob_direction = 1

# Grass
grass = pygame.Rect(300,200,200,150)

# Trees
trees = [
    pygame.Rect(200,150,60,60),
    pygame.Rect(450,350,60,60),
    pygame.Rect(600,100,60,60),
    pygame.Rect(150,400,60,60)
]

# NPC
npc = pygame.Rect(650,450,40,40)

# Grass particles
grass_particles = []

font = pygame.font.SysFont(None,28)
message = ""

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if player.colliderect(npc):
                    message = "Hello trainer! Welcome to DevMon!"

    keys = pygame.key.get_pressed()

    old_x = player.x
    old_y = player.y

    speed = 5
    if player.colliderect(grass):
        speed = 3

    moving = False

    if keys[pygame.K_LEFT]:
        player.x -= speed
        moving = True

    if keys[pygame.K_RIGHT]:
        player.x += speed
        moving = True

    if keys[pygame.K_UP]:
        player.y -= speed
        moving = True

    if keys[pygame.K_DOWN]:
        player.y += speed
        moving = True

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

    # NPC message
    if not player.colliderect(npc):
        message = ""

    # Bounce animation update
    if moving:
        bob_offset += 0.5 * bob_direction
        if abs(bob_offset) > 3:
            bob_direction *= -1
    else:
        bob_offset = 0

    # Grass particles spawn
    if player.colliderect(grass) and moving:
        if random.randint(1,8) == 1:
            particle = {
                "x": player.centerx + random.randint(-10,10),
                "y": player.bottom - 5,
                "radius": random.randint(2,4),
                "life": 20
            }
            grass_particles.append(particle)

    # Random encounter
    if player.colliderect(grass):
        if random.randint(1,150) == 1:
            print("🌟 A wild Pokémon appeared!")

    # Drawing
    screen.fill((100,200,100))

    pygame.draw.rect(screen,(0,0,0),(0,0,MAP_WIDTH,MAP_HEIGHT),5)

    screen.blit(grass_img,grass)

    for tree in trees:
        screen.blit(tree_img,tree)

    screen.blit(npc_img,npc)

    # Draw player with bounce
    screen.blit(player_img, (player.x, player.y + bob_offset))

    # Draw grass particles
    for particle in grass_particles[:]:
        particle["y"] -= 0.5
        particle["life"] -= 1

        pygame.draw.circle(
            screen,
            (50,150,50),
            (int(particle["x"]), int(particle["y"])),
            particle["radius"]
        )

        if particle["life"] <= 0:
            grass_particles.remove(particle)

    # Dialogue
    if message:
        text = font.render(message,True,(0,0,0))
        screen.blit(text,(20,560))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()