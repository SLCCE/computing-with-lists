import turtle

screen = turtle.Screen()
# draws the board and message
t = turtle.Turtle()
# draws the shapes
t2 = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.up()
t2.hideturtle()
t2.speed(0)
t2.up()

# square length, board length
SQ = 80
BL = 200

def draw_segment(x1, y1, x2, y2):
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)
    t.up()

# ==============================================================================================================================
# ==============================================================================================================================
# ==============================================================================================================================
def draw_board():
    '''
    Exercise: Draw the game board!
    draw_segment(a, b, c, d) draws a segment from the point (a, b) to (c, d)
    Use the draw_segment function to draw the 4 segments:
    horizontal lines: 
        (-200, 80) to (200, 80)
        (-200, -80) to (200, -80)
    vertical lines:
        (-80, -200) to (-80, 200)
        (80, -200) to (80, 200)
    The first one has already been done as an example
    '''
    # horizontal
    draw_segment(-200, 80, 200, 80)
    # ...
    # vertical
    # ...
    # ...
# ==============================================================================================================================
# ==============================================================================================================================
# ==============================================================================================================================

def determine_square(x, y):
    '''
    1 2 3
    4 5 6
    7 8 9
    '''
    # left column
    if -BL <= x < -SQ:
        if y > SQ:
            return 1
        elif -SQ <= y <= SQ:
            return 4
        else:
            return 7        
    # middle
    elif -SQ <= x <= SQ:
        if y > SQ:
            return 2
        elif -SQ <= y <= SQ:
            return 5
        else:
            return 8
    # right column
    elif SQ < x <= BL:
        if y > SQ:
            return 3
        elif -SQ <= y <= SQ:
            return 6
        else:
            return 9
    return 10

def check_win(board):
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0]:
                return board[i][0]
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i]:
                return board[0][i]
    # check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0]:
            return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[1][1]:
            return board[1][1]

    # check no squares left
    if not any(board[i][j] == 0 for i in range(3) for j in range(3)):
        return 0  # tie
    # noSquares = True
    # for i in range(3):
    #     for j in range(3):
    #         if board[i][j] != 0:
    #             noSquares = False
    # if noSquares:
    #     return 0

    # game keeps going
    return 3

def draw_symbol(turn, row, col):
    # center of the chosen square
    x_center = 2 * (-BL + 1.5 * SQ + col * SQ)
    y_center = 2 * (BL - 1.5 * SQ - row * SQ)

    if turn == 1:  # X
        size = SQ // 2 - 10
        t2.up()
        t2.goto(x_center - size, y_center - size)
        t2.down()
        t2.goto(x_center + size, y_center + size)
        t2.up()
        t2.goto(x_center - size, y_center + size)
        t2.down()
        t2.goto(x_center + size, y_center - size)
        t2.up()
    else:  # O
        radius = SQ // 2 - 10
        t2.up()
        t2.goto(x_center, y_center - radius)
        t2.down()
        t2.circle(radius)
        t2.up()

def show_message(text):
    t.up()
    t.goto(0, -BL - 40)
    t.write(text, align="center", font=("Arial", 16, "bold"))

# Define what happens when you click
def handle_click(x, y):
    global turn, gameOn

    if not gameOn:
        return
    box = determine_square(x, y)
    if box == 10:
        return
    # convert 1–9 box to row/col
    row = (box - 1) // 3
    col = (box - 1) % 3
    if state[row][col]:
        return
    state[row][col] = turn
    draw_symbol(turn, row, col)

    result = check_win(state)
    if result == 0:
        gameOn = False
        show_message("It's a tie!")
        return
    elif result == 1:
        gameOn = False
        show_message("Player X wins!")
        return
    elif result == 2:
        gameOn = False
        show_message("Player O wins!")
        return

    # 1 -> 2 and 2 -> 1
    turn = 3 - turn

turn = 1
state = [[0] * 3 for _ in range(3)]
gameOn = True
draw_board()

# Register the click handler
screen.onscreenclick(handle_click)

# Keep the window open until closed
screen.mainloop()  # event loop
