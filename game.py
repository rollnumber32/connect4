import socket, pickle, pygame, sys
from support import refresh, display_result
from algo import check_for_win

HOST = "localhost"
PORT = 3000


def connect():

    pygame.init()
    screen = pygame.display.set_mode((700, 600))
    pygame.display.set_caption("Connect4")
    player = 0
    grid = []
    won = False

    try:
        player = 1
        while True:
            s = socket.socket()
            s.connect((HOST, PORT))
            data = s.recv(4096)
            grid = pickle.loads(data)
            if grid == 0:
                break
            while refresh(screen, player, grid):
                continue
            refresh(screen, player, grid)
            won = check_for_win(grid, player)
            if won:
                grid = 0
            data = pickle.dumps(grid)
            s.send(data)
            if grid == 0:
                break
    except:
        player = 2
        # Initialize grid
        for i in range(0, 6):
            row = []
            for j in range(0, 7):
                row.append(0)
            grid.append(row)

        s = socket.socket()
        s.bind((HOST, PORT))
        s.listen()

        refresh(screen, player, grid)
        while True:
            c, addr = s.accept()
            data = pickle.dumps(grid)
            c.send(data)
            if grid == 0:
                break
            data = c.recv(4096)
            grid = pickle.loads(data)
            if grid == 0:
                break
            while refresh(screen, player, grid):
                continue
            refresh(screen, player, grid)
            won = check_for_win(grid, player)
            if won:
                grid = 0

    outcome = "lose!"
    if won:
        outcome = "win!!!"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        display_result(screen, outcome)


connect()
