import math

def next_move(posx, posy, dimx, dimy, board):
    if (board[posx][posy]).lower() == 'd':
        print("CLEAN")
        return

    closest_dirty_cell = (dimx + 1, dimy + 1)
    dist = euclidean_distance([posx, posx], closest_dirty_cell)
    for i in range(dimx):
        for j in range(dimy):
            if str(board[i][j]).lower() == 'd':
                d = euclidean_distance([posx, posy], [i, j])
                if d < dist:
                    closest_dirty_cell = (i, j)
                    dist = d

    move = "NONE"
    x = closest_dirty_cell[1] - posy
    y = closest_dirty_cell[0] - posx

    if x > 0:
        move = "RIGHT"
        posy += 1
    elif x < 0:
        move = "LEFT"
        posy -= 1
    elif y > 0:
        move = "DOWN"
        posx += 1
    elif y < 0:
        move = "UP"
        posx -= 1

    print(move)


def euclidean_distance(plot1, plot2):
    return math.sqrt((plot1[0] - plot2[0])**2 + (plot1[1]-plot2[1])**2)




mx = 0
my = 0
h = 5
w = 5
b = [['b', 'd', '-', '-', '-'], ['-', 'd', '-', '-', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', 'd', '-', 'd']]
next_move(mx, my, w, h, b)
