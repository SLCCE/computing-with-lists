from enum import Enum 

# Enumeration for the two different tile colors
class Tile(Enum):
    RED = 1
    YELLOW = 2

# Number of peices in a row to win
WINNING_NUMBER = 4
# Number of rows in the game board
ROWS = 6
# Number of columns in the game board
COLUMNS = 7
# -_ --> _-


# Status for if the game has been won or not
gameWon = False
#Status for if the game has been drawn or not
gameDraw = False
# Status for the current player's turn
currentPlayer = Tile.RED
# List to hold the board, will be made of COLUMNS number of lists
board = []


def main():
    # Tells main that these variable are global and allow main to access them
    global gameWon, currentPlayer, board
    # Create columns of board by adding a list to represent each column to be used as a stack
    for i in range(COLUMNS):
        board.append([])

    print('Welcome to Connect 4!')

    # Take player input while a player has not won yet
    while not gameWon and not gameDraw:
        # Let the player see the current board
        printBoard()

        # Ask for current players input. input returns a string
        columnSelection = input('Select a column to place your tile. It is ' + currentPlayer.name + ' Player\'s turn')

        # Try to convert columnSelection to an int
        try: 
            columnSelection = int(columnSelection)
        except ValueError:
            continue
        

        # Check that columnSelection is an integer and can index into board
        while not isValidInput(columnSelection):
            columnSelection = input('Invalid input selected. Try again.')
            try: 
                columnSelection = int(columnSelection)
            except ValueError:
                continue

        # Add a tile to the top of the specifed column
        board[columnSelection].append(currentPlayer)

        # Call checkForWin, while passing the indexes of the column and the row
        gameWon = checkForWin(columnSelection, len(board[columnSelection]) - 1)

        gameDraw = checkForDraw()

        # Switch the player turn if the game has not been won yet
        if currentPlayer is Tile.RED and not gameWon:
            currentPlayer = Tile.YELLOW
        elif currentPlayer is Tile.YELLOW and not gameWon:
            currentPlayer = Tile.RED

    # Print final board
    printBoard()
    # Print out the winner
    if gameWon: 
        print(currentPlayer.name + ' Player won!')
    elif gameDraw:
        # EXERCISE: print a statement saying that game is a draw!
        pass
    return



# Helper function to print our the current game board
def printBoard():
    # Construct and print a string to label the columns
    numberLine = ''
    for i in range(COLUMNS):
        # Print correct spacing incase number of columns is greater then 9
        if (i <= 9):
            numberLine += '  ' + str(i)
        else:
            numberLine += ' ' + str(i)
    print(numberLine)

    # Print top dividing line
    print('---' * COLUMNS + '-')

    # Track row index to print from top downward
    index = ROWS - 1
    while index >= 0:
        rowLine = '|'
        # For each column in board add the tile to the rowLine string
        for column in board:
            # If the column is long enough check for what color tile if not print a space
            if len(column) >= index + 1:
                # Ternary operator. If the current index of the board is a RED Tile set 
                # tile to be a red unicode circle if not set it to a yellow unicode circle
                tile = '\U0001F534' if column[index] == Tile.RED else '\U0001F7E1'
                # F-string: same as rowLine += tile + "|"
                rowLine += f"{tile}|"
            else:
                # Prints two spaces because emojis are two character's wide
                rowLine += "  |"
        # Decrement index to build next row
        index -= 1
        # Print the string we just built that represents are row of the game board
        print(rowLine)



# Helper function that checks that columnSelection is a integer and in the bounds of the board. 
# Will return false if columnSelection is invalid and true if its valid
def isValidInput(columnSelection):
    # Check that columnSelection is an int, not less than zero and is less than the number of columns
    if not isinstance(columnSelection, int) or columnSelection < 0 or columnSelection >= len(board):
        return False
    # Check that selected column still has space to hold the tile
    elif len(board[columnSelection]) >= ROWS:
        return False
    else: 
        return True

# Helper function that returns true if the last move resulted in a win, false otherwise
def checkForWin(col, row):
    # Get the current color
    color = board[col][row]
    
    # Delegate to other helper functions, if any result in a win, a player has won
    return isVertWin(col, row, color) or isHorizWin(col, row, color) or isDiagWin(col, row, color)
    
# Helper function that checks for a vertical win. Returns true if vertical win is found, false otherwise
def isVertWin (col, row, color):
    # Start at 1 because we already know the last played tile is the same color of the last played tile
    verticalCount = 1
    index = row - 1
    # While the tiles under the last played tile are of the same color increment verticalCount
    while index >= 0 and board[col][index] is color:
        index -= 1
        verticalCount += 1

    if verticalCount >= WINNING_NUMBER:
        return True
    
    return False

# Helper function to check for a horizontal win. Returns true if horizontal win is found, false otherwise
def isHorizWin (col, row, color):
    # Start at 1 because we already know the last played tile is the same color of the last played tile
    horizontalCount = 1
    
    index = col - 1
    # Check left while not going out of bounds and the tile matches the last played tile
    while index >= 0 and row < len(board[index]) and board[index][row] is color:
        index -= 1
        horizontalCount += 1
    # Check right while not going out of bounds and the tile matches the last played tile
    index = col + 1
    while index < len(board) and row < len(board[index]) and board[index][row] is color:
        index += 1
        horizontalCount += 1

    if horizontalCount >= WINNING_NUMBER:
        return True
    
    return False
    
def isDiagWin (col, row, color):
    # Start at 1 because we already know the last played tile is the same color of the last played tile
    diagCount = 1

    # Check bottom left
    xIndex = col - 1
    yIndex = row - 1
    # Check left and down while not going out of bounds and the tile matches the last played tile
    while xIndex >= 0 and yIndex >=0 and yIndex < len(board[xIndex]) and board[xIndex][yIndex] is color:
        xIndex -= 1
        yIndex -= 1
        diagCount += 1
    
    # Check top right
    xIndex = col + 1
    yIndex = row + 1
    # Check right and up while not going out of bounds and the tile matches the last played tile
    while xIndex < len(board) and yIndex < len(board[xIndex]) and board[xIndex][yIndex] is color:
        xIndex += 1
        yIndex += 1
        diagCount += 1

    if diagCount >= WINNING_NUMBER:
        return True
    
    # Reset diagCount
    diagCount = 1

     # Check top left
    xIndex = col - 1
    yIndex = row + 1
    # Check left and up while not going out of bounds and the tile matches the last played tile
    while xIndex >= 0 and yIndex < len(board[xIndex]) and board[xIndex][yIndex] is color:
        xIndex -= 1
        yIndex += 1
        diagCount += 1
    
    # Check bottom right
    xIndex = col + 1
    yIndex = row - 1
    # Check right and down while not going out of bounds and the tile matches the last played tile
    while xIndex < len(board) and yIndex >= 0 and yIndex < len(board[xIndex]) and board[xIndex][yIndex] is color:
        xIndex += 1
        yIndex -= 1
        diagCount += 1

    if diagCount >= WINNING_NUMBER:
        return True
    
    return False

def checkForDraw():
    # EXERCISE: make sure that each column has 6 pieces
    # return True if the board is full. Since we already check for a win, it's a draw
    # return False if the board isn't full
    pass

# Call the main function
if __name__ == '__main__':
    main()

