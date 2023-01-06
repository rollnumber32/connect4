import pygame

# Initializing
pygame.init()

# Setting screen size
screen = pygame.display.set_mode((800, 600))

# Game name
pygame.display.set_caption("Connect4")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
