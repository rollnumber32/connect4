import pygame
import math

# Game starts
def start():

    # Initializing
    pygame.init()

    # Setting screen size
    screen = pygame.display.set_mode((700, 600))

    # Game name
    pygame.display.set_caption("Connect4")

    # Game state
    grid = []
    for i in range(0, 6):
        row = []
        for j in range(0, 7):
            row.append(0)
        grid.append(row)

    player = 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                column = math.floor(pos[0] / 100)
                row = _handle_click(grid, column, player)
                if _check_for_win(grid, row, column):
                    print(player, "wins")
                if player == 1:
                    player = 2
                else:
                    player = 1

        screen.fill((0, 128, 255))
        _draw_grid(screen, grid)
        pygame.display.update()


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


def _handle_click(grid, column, player):
    i = 5
    while i >= 0:
        if grid[i][column] == 0:
            grid[i][column] = player
            return i
        i = i - 1


def _check_for_win(grid, r, c):
    count = 1
    while r + count <= 5 and grid[r + count][c] == grid[r][c]:
        count += 1
        if count == 4:
            return True

    count = 1
    while c + count <= 6 and grid[r][c + count] == grid[r][c]:
        count += 1
        if count == 4:
            return True

    count = 1
    while (
        r + count <= 5 and c + count <= 6 and grid[r + count][c + count] == grid[r][c]
    ):
        count += 1
        if count == 4:
            return True

    count = 1
    while (
        r + count <= 5 and c - count >= 0 and grid[r + count][c - count] == grid[r][c]
    ):
        count += 1
        if count == 4:
            return True

    return False


start()
