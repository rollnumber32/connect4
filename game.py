import pygame
import math
import copy

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
    winner = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                column = math.floor(pos[0] / 100)
                row = _handle_click(grid, column, player)
                if row == -1:
                    continue
                if _check_for_win(grid, player):
                    winner = True
                    continue
                if player == 1:
                    player = 2
                else:
                    player = 1

        screen.fill((0, 128, 255))
        _draw_grid(screen, grid)
        if winner:
            _execute_win(screen, player)
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
    return -1


def _check_for_win(grid, player):
    gc = copy.deepcopy(grid)

    for i in range(0, 6):
        for j in range(0, 7):
            if (
                gc[i][j] == player
                and _check_lr(gc, i, j, player)
                or _check_tb(gc, i, j, player)
                or _check_lrd(gc, i, j, player)
                or _check_rld(gc, i, j, player)
            ):
                return True

    return False


def _check_lr(grid, i, j, player):
    jc = j
    count = 0
    while jc <= 6:
        if grid[i][jc] == player:
            count += 1
        else:
            break
        jc += 1

    if count >= 4:
        return True

    return False


def _check_tb(grid, i, j, player):
    ic = i
    count = 0
    while ic <= 5:
        if grid[ic][j] == player:
            count += 1
        else:
            break
        ic += 1

    if count >= 4:
        return True

    return False


def _check_lrd(grid, i, j, player):
    ic = i
    jc = j
    count = 0
    while ic <= 5 and jc <= 6:
        if grid[ic][jc] == player:
            count += 1
        else:
            break
        ic += 1
        jc += 1

    if count >= 4:
        return True

    return False


def _check_rld(grid, i, j, player):
    ic = i
    jc = j
    count = 0
    while ic <= 5 and jc >= 0:
        if grid[ic][jc] == player:
            count += 1
        else:
            break
        ic += 1
        jc -= 1

    if count >= 4:
        return True

    return False


def _execute_win(screen, player):
    font = pygame.font.Font("roboto.ttf", 32)
    text = font.render(
        "Player " + str(player) + " wins", True, (0, 0, 0), (255, 255, 255)
    )
    text_rect = text.get_rect()
    text_rect.center = (350, 300)
    screen.blit(text, text_rect)


start()
