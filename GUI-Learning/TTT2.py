import random

from tkinter import *
from tkinter import ttk


def main_window():
    root.title('Tic Tac Toe')
    remove_widgets()
    global frame

    frame = ttk.Frame(root, width=250, height=150, relief='groove')
    frame.pack_propagate(False)
    frame.pack(padx=25, pady=75)

    play = ttk.Button(frame, text='Play', command=lambda: play_menu(do=0))
    play.pack(side='top', pady=(50, 0))

    qb = ttk.Button(frame, text="Quit", command=root.destroy)
    qb.pack(side='top', pady=(0, 50))


def play_menu(do):
    root.title('Tic Tac Toe')
    remove_widgets()
    if do == 'redeclare':
        redeclare_vars()

    global frame

    label = ttk.Label(root, text='Choose your side', font=('French Script MT', 20))
    label.pack(side='top', pady=(25, 0))

    frame = ttk.Frame(root, width=250, height=150, relief='groove')
    frame.pack_propagate(False)
    frame.pack(padx=25, pady=25)

    player_x = ttk.Button(frame, text='X', command=lambda: game(pl='X'))
    player_x.grid(column=0, row=0, padx=(5, 0), pady=(5, 0))

    player_o = ttk.Button(frame, text='O', command=lambda: game(pl='O'))
    player_o.grid(column=1, row=0, padx=(0, 5), pady=(5, 0))

    back = ttk.Button(frame, text='Back', command=main_window)
    back.grid(column=0, row=1, sticky=(E, W), padx=(5, 5), pady=(0, 5), columnspan=2)


def game(pl=None):
    root.title('Tic Tac Toe')
    remove_widgets()

    global frame, canvas, player, computer, move, stop_game

    frame = ttk.Frame(root, width=650, height=700)
    frame.pack_propagate(False)
    frame.pack()

    canvas = Canvas(frame, width=600, height=600)
    canvas.pack(side='top', pady=(25, 0))

    restart = ttk.Button(frame, text='Restart', command=lambda: play_menu(do='redeclare'))
    restart.pack(side='bottom', pady=20)

    draw_board()
    canvas.bind('<Button-1>', square_selector)

    if pl == 'X':
        player = 'X'
        computer = 'O'
        move = 'player'
    elif pl == 'O':
        player = 'O'
        computer = 'X'
        move = 'computer'
        computer_move()


def remove_widgets():
    for widget in root.winfo_children():
        widget.destroy()


def square_status_lib(square):
    global statusLib, player
    status = None

    if player == 'X':
        status = 'X'
    elif player == 'O':
        status = 'O'
    statusLib[square-1] = status


def square_selector(event):
    if 1 <= event.x <= 199:
        if 1 <= event.y <= 199:
            player_move(square=1)
    elif 1 <= event.x <= 199:
        if 201 <= event.y <= 399:
            player_move(square=2)
    elif 1 <= event.x <= 199:
        if 401 <= event.y <= 599:
            player_move(square=3)
    elif 201 <= event.x <= 399:
        if 1 <= event.y <= 199:
            player_move(square=4)
    elif 201 <= event.x <= 399:
        if 201 <= event.y <= 399:
            player_move(square=5)
    elif 201 <= event.x <= 399:
        if 401 <= event.y <= 599:
            player_move(square=6)
    elif 401 <= event.x <= 599:
        if 1 <= event.y <= 199:
            player_move(square=7)
    elif 401 <= event.x <= 599:
        if 201 <= event.y <= 399:
            player_move(square=8)
    elif 401 <= event.x <= 599:
        if 401 <= event.y <= 599:
            player_move(square=9)


def computer_move():
    global move, x1, y1, x2, y2
    status, a = 0, 0

    while status is not None:
        a = random.randint(1, 9)
        status = statusLib[a-1]
        x1, y1, x2, y2 = squareLib[a - 1][0], squareLib[a - 1][1], squareLib[a - 1][2], squareLib[a - 1][3]
    if computer == 'X':
        draw_move()
        statusLib[a-1] = 'X'
    elif computer == 'O':
        draw_move()
        statusLib[a-1] = 'O'
    end_game()
    if not stop_game:
        move = 'player'


def player_move(square):
    global x1, y1, x2, y2, move, squareLib, stop_game

    if statusLib[square-1] is None:
        x1, y1, x2, y2 = squareLib[square-1][0], squareLib[square-1][1], squareLib[square-1][2], squareLib[square-1][3]
        draw_move()
        square_status_lib(square=square)
        end_game()
        if not stop_game:
            move = 'computer'
            computer_move()


def draw_move():
    global player, x1, y1, x2, y2, canvas, move

    if move == 'player':
        if player == 'X':
            canvas.create_line(x1, y1, x2, y2)
            canvas.create_line(x1, y2, x2, y1)
        elif player == 'O':
            canvas.create_oval(x1, y1, x2, y2)
    elif move == 'computer':
        if computer == 'X':
            canvas.create_line(x1, y1, x2, y2)
            canvas.create_line(x1, y2, x2, y1)
        elif computer == 'O':
            canvas.create_oval(x1, y1, x2, y2)


def draw_board():
    global canvas
    canvas.create_line(0, 200, 600, 200)
    canvas.create_line(0, 400, 600, 400)
    canvas.create_line(200, 0, 200, 600)
    canvas.create_line(400, 0, 400, 600)


def check_end_game():
    global tie, stop_game, fin

    if statusLib[0] == statusLib[1] == statusLib[2] == 'X' or statusLib[0] == statusLib[1] == statusLib[2] == 'O':
        stop_game, fin = True, 1
    elif statusLib[3] == statusLib[4] == statusLib[5] == 'X' or statusLib[3] == statusLib[4] == statusLib[5] == 'O':
        stop_game, fin = True, 2
    elif statusLib[6] == statusLib[7] == statusLib[8] == 'X' or statusLib[6] == statusLib[7] == statusLib[8] == 'O':
        stop_game, fin = True, 3
    elif statusLib[0] == statusLib[3] == statusLib[6] == 'X' or statusLib[0] == statusLib[3] == statusLib[6] == 'O':
        stop_game, fin = True, 4
    elif statusLib[1] == statusLib[4] == statusLib[7] == 'X' or statusLib[1] == statusLib[4] == statusLib[7] == 'O':
        stop_game, fin = True, 5
    elif statusLib[2] == statusLib[5] == statusLib[8] == 'X' or statusLib[2] == statusLib[5] == statusLib[8] == 'O':
        stop_game, fin = True, 6
    elif statusLib[2] == statusLib[4] == statusLib[6] == 'X' or statusLib[2] == statusLib[4] == statusLib[6] == 'O':
        stop_game, fin = True, 7
    elif statusLib[0] == statusLib[4] == statusLib[8] == 'X' or statusLib[0] == statusLib[4] == statusLib[8] == 'O':
        stop_game, fin = True, 8
    elif all(k is not None for k in statusLib):
        stop_game, tie, fin = True, True, 0
    else:
        stop_game, fin = False, 0


def end_game():
    global stop_game, tie, canvas
    check_end_game()
    text = ''

    if stop_game:
        canvas.unbind('<Button-1>')
        if move == 'player' and not tie:
            text = 'You win'
        elif move == 'computer' and not tie:
            text = 'You lose'
        elif tie:
            text = 'It\'s a tie'

        finisher()
        canvas.create_text(300, 300, text=text, font=('French Script MT', 50), fill='#000000')

    elif not stop_game:
        pass


def finisher():
    global fin
    x3, y3, x4, y4 = 0, 0, 0, 0

    if fin != 0:
        if fin == 1:
            x3, y3, x4, y4 = 100, 100, 100, 500
        elif fin == 2:
            x3, y3, x4, y4 = 300, 100, 300, 500
        elif fin == 3:
            x3, y3, x4, y4 = 500, 100, 500, 500
        elif fin == 4:
            x3, y3, x4, y4 = 100, 100, 500, 100
        elif fin == 5:
            x3, y3, x4, y4 = 100, 300, 500, 300
        elif fin == 6:
            x3, y3, x4, y4 = 100, 500, 500, 500
        elif fin == 7:
            x3, y3, x4, y4 = 100, 500, 500, 100
        elif fin == 8:
            x3, y3, x4, y4 = 100, 100, 500, 500
        canvas.create_line(x3, y3, x4, y4)
    elif fin == 0:
        pass


def redeclare_vars():
    global statusLib, myVal, x1, x2, y1, y2, canvas, move, fin, stop_game, tie
    statusLib = []
    myVal = None
    for l in range(0, 9):
        statusLib.append(myVal)
    x1, y1, x2, y2, canvas, move, fin = 0, 0, 0, 0, None, '', 0
    stop_game, tie = False, False


root = Tk()
root.minsize(width=300, height=300)

statusLib = []
myVal = None
for i in range(0, 9):
    statusLib.append(myVal)
x1, y1, x2, y2, canvas, move, fin = 0, 0, 0, 0, None, '', 0
stop_game, tie = False, False
game_mode = IntVar()

squareLib = [
             [20, 20, 180, 180],
             [20, 220, 180, 380],
             [20, 420, 180, 580],
             [220, 20, 380, 180],
             [220, 220, 380, 380],
             [220, 420, 380, 580],
             [420, 20, 580, 180],
             [420, 220, 580, 380],
             [420, 420, 580, 580]
            ]

main_window()
root.mainloop()