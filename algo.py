import copy


def check_for_win(grid, player):
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
