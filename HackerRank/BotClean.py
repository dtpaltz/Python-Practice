import math


def next_move(posr, posc, board):
    if (board[posr][posc]).lower() == 'd':
        print("CLEAN")
        return

    n = len(board[0])
    closest_dirty_cell = (n + 1, n + 1)
    dist = euclidean_distance([posr, posc],  closest_dirty_cell)
    for i in range(n):
        for j in range(n):
            if str(board[i][j]).lower() == 'd':
                d = euclidean_distance([posr, posc], [i, j])
                if d < dist:
                    closest_dirty_cell = (i, j)
                    dist = d

    move = "NONE"
    x = closest_dirty_cell[1] - posc
    y = closest_dirty_cell[0] - posr

    if x > 0:
        move = "RIGHT"
        posc += 1
    elif x < 0:
        move = "LEFT"
        posc -= 1
    elif y > 0:
        move = "DOWN"
        posr += 1
    elif y < 0:
        move = "UP"
        posr -= 1

    print(move)


def euclidean_distance(plot1, plot2):
    return math.sqrt((plot1[0] - plot2[0])**2 + (plot1[1]-plot2[1])**2)




r = 0
c = 0
grid = ['d---d', '-d--d', '--dd-', '--d--', '----d']
next_move(r, c, grid)
