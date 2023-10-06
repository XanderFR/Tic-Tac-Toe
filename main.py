# Written by Alexander Dave Flores Respicio
from Player import Player

# Global constants
EX = "X"
OH = "O"
NINE = 9


def printWelcomeBanner():  # Prints the welcome banner to the game
    for _ in range(0, 22):
        print("*", end="")
    print("\nWELCOME TO TIC-TAC-TOE")
    for _ in range(0, 22):
        print("*", end="")
    print()


def printInstructions():  # Prints the instructions for the game
    print("Welcome to a Python-written 2-player Tic-Tac-Toe game.")
    print("Player moves will be made by entering a number between 0 - 8.")
    print("The numbers correspond to the following places on the board as illustrated:\n")
    print("0 | 1 | 2")
    for _ in range(0, NINE):
        print("-", end="")
    print("\n3 | 4 | 5")
    for _ in range(0, NINE):
        print("-", end="")
    print("\n6 | 7 | 8\n")


def getPlayerNames():
    playerOneName = input("Enter the Player 1 name: ")
    playerTwoName = input("Enter the Player 2 name: ")
    return playerOneName, playerTwoName


def askPosition():  # Gets and returns the player's desired square position
    question = "Which position do you want? (0 to 8): "
    positionNumber = None
    # While loop that ensures human players enter a valid square position
    while positionNumber not in range(0, NINE):
        positionNumber = int(input(question))
    return positionNumber


def whichPiece(player1, player2):  # Determines which player gets which symbol
    question = "Do you want to go first? (y / n): "
    playerOneGoFirst = None
    # While loop that ensures player answers with a "y" or a "n"
    while playerOneGoFirst not in ("y", "n"):
        playerOneGoFirst = input(question).lower()
    if playerOneGoFirst == "y":  # Player 1 goes first
        print(f"\n{player1.getName()} makes the first move.")
        player1Symbol = EX
        player2Symbol = OH
    else:
        print(f"\n{player2.getName()} makes the first move.")  # Player 2 goes first
        player1Symbol = OH
        player2Symbol = EX
    return player1Symbol, player2Symbol  # Returns a pair of symbols


def newBoard():
    # Prepares list of empty board spaces
    board = []
    for space in range(NINE):
        board.append(" ")
    return board


def displayBoard(board):
    # Presents the board list and presents it as a 3x3 grid
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    for _ in range(0, NINE):
        print("-", end="")
    print(f"\n{board[3]} | {board[4]} | {board[5]}")
    for _ in range(0, NINE):
        print("-", end="")
    print(f"\n{board[6]} | {board[7]} | {board[8]}\n")


def validMoves(board):
    # Returns a list of numbers corresponding to blank squares on the game board
    moveList = []
    for square in range(NINE):
        if board[square] == " ":
            moveList.append(square)
    return moveList


def winningPlayer(board):
    # List of winning symbol sequences
    winningMoves = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )

    for row in winningMoves:
        # If one of the board sequences in winningMoves have the same symbols in them
        if board[row[0]] == board[row[1]] == board[row[2]] != " ":
            winningSymbol = board[row[0]]  # Prepare and return the symbol that won the game
            return winningSymbol

    if " " not in board:  # If the game board is full of characters
        return "Tie"

    return None


def humanMove(board, player):
    validMoveList = validMoves(board)  # Prepare the list of open board squares
    position = None
    # While loop that ensures player chooses a blank square position on the board
    while position not in validMoveList:
        position = askPosition()

        if position not in validMoveList:  # If block that lets the player know a square is taken
            print(f"\nThe square is already occupied, {player.getName()}. Pick another one.\n")
    return position


def nextTurn(turn):  # Function that helps determine whose turn it is
    if turn == EX:
        return OH
    else:
        return EX


def congrats(winnerSymbol, player1, player2):  # Prints who won or if the game ended with a tie
    # Compare the game winning symbol with the player symbols
    if winnerSymbol == player1.getSymbol():
        print(f"{player1.getName()} won!")
    elif winnerSymbol == player2.getSymbol():
        print(f"{player2.getName()} won!")
    elif winnerSymbol == "Tie":
        print("Tie")


def main():
    # Prints the welcome banner and instructions
    printWelcomeBanner()
    printInstructions()

    # Instantiate Player objects
    player1 = Player()
    player2 = Player()

    # Get the names of the players
    player1Name, player2Name = getPlayerNames()
    player1.setName(player1Name)
    player2.setName(player2Name)

    # Determine which player gets which game symbol
    player1Symbol, player2Symbol = whichPiece(player1, player2)
    player1.setSymbol(player1Symbol)
    player2.setSymbol(player2Symbol)

    turn = EX  # Represents who goes first

    # Prepare and display the game board
    board = newBoard()
    displayBoard(board)

    while not winningPlayer(board):  # While there is no winning player symbol
        # If / else blocks that say whose turn it is, gets the player's desired board position,
        # and puts the player's symbol on the board
        if turn == player1.getSymbol():
            print(f"{player1.getName()}'s turn")
            move = humanMove(board, player1)
            board[move] = player1.getSymbol()
        else:
            print(f"{player2.getName()}'s turn")
            move = humanMove(board, player2)
            board[move] = player2.getSymbol()
        displayBoard(board)  # Show the current board
        turn = nextTurn(turn)  # It's the other player's turn

    winner = winningPlayer(board)  # Represents the game ending / winning symbol
    congrats(winner, player1, player2)  # Present a congratulatory message depending on whom won

main()
