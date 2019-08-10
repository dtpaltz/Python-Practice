

# The first line of the input is N (<100), the size of the board (NxN)
# The second line of the input contains two space separated integers, which is the position of the bot.

def nextMove(n,r,c,grid):
    px = 0
    py = 0
    mx = c
    my = r
    for i in range(n):
        for j in range(n):
            if str(grid[i][j]).lower() == 'p':
                px = j
                py = i

    move = "NONE"
    x = px - mx
    y = py - my

    if x > 0:
        move = "RIGHT"
        mx += 1
    elif x < 0:
        move = "LEFT"
        mx -= 1
    elif y > 0:
        move = "DOWN"
        my += 1
    elif y < 0:
        move = "UP"
        my -= 1

    return move







n = 5
r = 2
c = 3
grid = ['-----', '-----', 'p--m-', '-----', '-----']


print(nextMove(n, r, c, grid))

