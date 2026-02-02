from enum import Enum 

class Tile(Enum):
    RED = 1
    YELLOW = 2


# Number of rows in the game board
ROWS = 6
# Number of columns in the game board
COLUMNS = 7
# -_ --> _-

# Number of peices in a row to win
WINNING_NUMBER = 4
# Status for if the game has been won or not
gameWon = False

currentPlayer = Tile.RED

board = []

def main():
    # Create columns of board
    for i in range(COLUMNS):
        board.append([])

    print('Welcome to Connect 4!')

    while not gameWon:
        printBoard()
        columnSelection = input('Select a column to place your tile. It is' + currentPlayer.name + 'Player\'s turn')
        

        # Check that columnSelection is and integer and can index into board
        while not isValidInput(columnSelection):
            columnSelection = input('Invalid input selected.')

        board[columnSelection].append(currentPlayer)

        gameWon = checkForWin(columnSelection, len(board[columnSelection]) - 1)

        if currentPlayer is Tile.RED and not gameWon:
            currentPlayer = Tile.YELLOW
        elif currentPlayer is Tile.YELLOW and not gameWon:
            currentPlayer = Tile.RED

    printBoard()
    print(currentPlayer.name + 'Player won!')




def printBoard():
    print('___' * COLUMNS)
    index = ROWS - 1
    while index > 0:
        rowLine = '|'
        for column in board:
            if len(column) >= index + 1:
                tile = 'X' if column[index] == Tile.RED else 'O'
                rowLine += f"{tile}|"
            else:
                rowLine += " |"




def isValidInput(columnSelection):
    if not isinstance(columnSelection, int) or columnSelection < 0 or columnSelection > len(board):
        return False
    elif len(board[columnSelection] >= ROWS):
        return False
    else: 
        return True


def checkForWin(col, row):
    color = board[col][row]
    
    return isVertWin(col, row, color) or isHorizWin(col, row, color) or isDiagWin(col, row, color)
    
    
def isVertWin (col, row, color):
    verticalCount = 0
    index = row
    while index >= 0 and board[col][index] is color:
        index -= 1
        verticalCount += 1
    if verticalCount >= WINNING_NUMBER:
        return True

def isHorizWin (col, row, color):
    horizontalCount = 0
    # Check left
    index = col
    while index >= 0 and board[index][row] is color:
        index -= 1
        horizontalCount += 1
    # Check right
    index = col
    while index < len(board) and board[index][row] is color:
        index += 1
        horizontalCount += 1

    if horizontalCount >= WINNING_NUMBER:
        return True
    
def isDiagWin (col, row, color):
    diagCount = 0

    # Check bottom left
    xIndex = col
    yIndex = row
    while xIndex >= 0 and yIndex >=0 and board[xIndex][yIndex] is color:
        xIndex -= 1
        yIndex -= 1
        diagCount += 1
    
    # Check top right
    xIndex = col
    yIndex = row
    while xIndex < len(board) and yIndex < len(board[xIndex]) and board[xIndex][yIndex] is color:
        xIndex += 1
        yIndex += 1
        diagCount += 1

    if diagCount >= WINNING_NUMBER:
        return True
    
    # Reset diagCount
    diagCount = 0

     # Check top left
    xIndex = col
    yIndex = row
    while xIndex >= 0 and yIndex < len(board[xIndex]) and board[xIndex][yIndex] is color:
        xIndex -= 1
        yIndex += 1
        diagCount += 1
    
    # Check bottom right
    xIndex = col
    yIndex = row
    while xIndex < len(board) and yIndex >= 0 and board[xIndex][yIndex] is color:
        xIndex += 1
        yIndex -= 1
        diagCount += 1

    if diagCount >= WINNING_NUMBER:
        return True
    


