helpAboutMove = """Move example: mn\n""" \
                """m - row (range from 0 to 2)\n"""\
                """n - column (range from 0 to 2)\n"""
move = '00'
matrixSymbol = [[['-','unlocked'] for i in range(3)] for i in range(3)]
symbols = {1:'x', 2:'o'}
player = 1
numMoves = 0

def reset():
    global player
    global numMoves

    for i in range(3):
        for j in range(3):
            matrixSymbol[i][j] = ['-', 'unlocked']
    player = 1
    numMoves = 0
    while True:
        yes = input("New game Y/N?")
        if yes == 'Y' or yes == 'y':
            print(helpAboutMove)
            printField()
            return True
        elif yes == 'N' or yes == 'n':
            return False

def printField():
    print("""  0 1 2 \n""" \
          """0 %c %c %c \n""" \
          """1 %c %c %c \n""" \
          """2 %c %c %c \n""" % \
          (matrixSymbol[0][0][0],matrixSymbol[0][1][0],matrixSymbol[0][2][0],\
           matrixSymbol[1][0][0],matrixSymbol[1][1][0],matrixSymbol[1][2][0],\
           matrixSymbol[2][0][0],matrixSymbol[2][1][0],matrixSymbol[2][2][0]))

def checkMove(func):
    def wrapper():
        global player
        global numMoves

        if len(move) == 2 and move[0].isdigit() and move[1].isdigit():
            row = int(move[0])
            column = int(move[1])
            if 0 <= row <= 2 and 0 <= column <= 2 and not matrixSymbol[row][column][1] == 'locked':
                matrixSymbol[row][column][0] = symbols[player]
                matrixSymbol[row][column][1] = 'locked'
                func()

                if player == 2: player = 1
                else:           player = 2

                numMoves += 1
            else:
                print("incorrect index\n")
        else:
            print("incorrect move\n")
    return wrapper

def checkResult():
    global numMoves
    global player

    if player == 2: playerLoc = 1
    else:           playerLoc = 2

    for i in range(3):
        if matrixSymbol[i][0][0] == matrixSymbol[i][1][0] == matrixSymbol[i][2][0] != '-':
            print(f"Player{playerLoc} WIN!!!")
            return True
    for i in range(3):
        if matrixSymbol[0][i][0] == matrixSymbol[1][i][0] == matrixSymbol[2][i][0] != '-':
            print(f"Player{playerLoc} WIN!!!")
            return True
    if (matrixSymbol[0][0][0] == matrixSymbol[1][1][0] == matrixSymbol[2][2][0] != '-') or \
       (matrixSymbol[0][2][0] == matrixSymbol[1][1][0] == matrixSymbol[2][0][0] != '-'):
       print(f"Player{playerLoc} WIN!!!")
       return True

    if numMoves >= 9:
        print("Draw")
        return True
    return False

@checkMove
def printFieldProcess():
    printField()

if(reset()):
    while(True):
        move = input(f"Player{player}:")
        printFieldProcess()
        if checkResult():
            if not reset():
                break
