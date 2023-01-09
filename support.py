import pygame, math, sys


def refresh(screen, player, grid):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            column = math.floor(pos[0] / 100)
            return _add_piece(grid, column, player)

    screen.fill((0, 128, 255))
    _draw_grid(screen, grid)
    pygame.display.update()

    return True


def _draw_grid(screen, grid):
    y = 50
    for row in grid:
        x = 50
        for cell in row:
            color = (0, 0, 0)
            if cell == 1:
                color = (255, 128, 0)
            elif cell == 2:
                color = (0, 255, 128)
            pygame.draw.circle(screen, color, (x, y), 40)
            x = x + 100
        y = y + 100


def _add_piece(grid, column, player):
    i = 5
    while i >= 0:
        if grid[i][column] == 0:
            grid[i][column] = player
            return False
        i = i - 1
    return True


def display_result(screen, outcome):
    font = pygame.font.Font("roboto.ttf", 32)
    text = font.render(f"You {outcome}", True, (0, 0, 0), (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (350, 300)
    screen.blit(text, text_rect)
    pygame.display.update()
