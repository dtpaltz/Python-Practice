

def displayPathtoPrincess(n, grid):
    px = 0
    py = 0
    mx = 0
    my = 0
    for i in range(n):
        for j in range(n):
            if str(grid[i][j]).lower() == 'p':
                px = j
                py = i
            if str(grid[i][j]).lower() == 'm':
                mx = j
                my = i

    while True:
        if px == mx and py == my:
            break

        x = px - mx
        y = py - my

        if x > 0:
            print("RIGHT")
            mx += 1
        elif x < 0:
            print("LEFT")
            mx -= 1
        elif y > 0:
            print("DOWN")
            my += 1
        elif y < 0:
            print("UP")
            my -= 1



m = 3
grid = ['---', '-m-', 'p--']
displayPathtoPrincess(m, grid)

