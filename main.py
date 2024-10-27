import random

GAME_SIZE = 4


def CreateMat():
    matt = []
    for i in range(GAME_SIZE):
        matt.append([])
        for j in range(GAME_SIZE):
            matt[i].append(0)
    return matt


def printGame(matt):
    for i in range(GAME_SIZE):
        print(matt[i])
    print('-----------')


def findEmptyNum(matt):
    count = 0
    for i in range(GAME_SIZE):
        for j in range(GAME_SIZE):
            if matt[i][j] != 0:
                count += 1
    return count


def getEmptyCellNum(matt):
    cells = []
    for i in range(GAME_SIZE):
        for j in range(GAME_SIZE):
            if matt[i][j] == 0:
                cells.append([i, j])
    cellNum = random.choice(cells)
    return cellNum


def findMax(matt):
    maxNum = 0
    for i in range(GAME_SIZE):
        for j in range(GAME_SIZE):
            if matt[i][j] > maxNum:
                maxNum = matt[i][j]
    return maxNum


def insertRandom(matt, cellNum, currentMax):
    bank = [2, 2, 4]
    matt[cellNum[0]][cellNum[1]] = random.choice(bank)


def firstMove(matt):
    matt[-1][-1] = 2


def gameDown(matt):
    for col in range(GAME_SIZE):

        for row in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0:
                current_row = row
                while current_row + 1 < GAME_SIZE and matt[current_row + 1][col] == 0:
                    matt[current_row + 1][col] = matt[current_row][col]
                    matt[current_row][col] = 0
                    current_row += 1

        for row in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0 and matt[row][col] == matt[row + 1][col]:
                matt[row + 1][col] *= 2
                matt[row][col] = 0

        for row in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0:
                current_row = row
                while current_row + 1 < GAME_SIZE and matt[current_row + 1][col] == 0:
                    matt[current_row + 1][col] = matt[current_row][col]
                    matt[current_row][col] = 0
                    current_row += 1


def gameUp(matt):
    for col in range(GAME_SIZE):

        for row in range(1, GAME_SIZE):
            if matt[row][col] != 0:
                current_row = row
                while current_row - 1 >= 0 and matt[current_row - 1][col] == 0:
                    matt[current_row - 1][col] = matt[current_row][col]
                    matt[current_row][col] = 0
                    current_row -= 1

        for row in range(1, GAME_SIZE):
            if matt[row][col] != 0 and matt[row][col] == matt[row - 1][col]:
                matt[row - 1][col] *= 2
                matt[row][col] = 0

        for row in range(1, GAME_SIZE):
            if matt[row][col] != 0:
                current_row = row
                while current_row - 1 >= 0 and matt[current_row - 1][col] == 0:
                    matt[current_row - 1][col] = matt[current_row][col]
                    matt[current_row][col] = 0
                    current_row -= 1


def gameLeft(matt):
    for row in range(GAME_SIZE):

        for col in range(1, GAME_SIZE):
            if matt[row][col] != 0:
                current_col = col
                while current_col - 1 >= 0 and matt[row][current_col - 1] == 0:
                    matt[row][current_col - 1] = matt[row][current_col]
                    matt[row][current_col] = 0
                    current_col -= 1

        for col in range(1, GAME_SIZE):
            if matt[row][col] != 0 and matt[row][col] == matt[row][col - 1]:
                matt[row][col - 1] *= 2
                matt[row][col] = 0

        for col in range(1, GAME_SIZE):
            if matt[row][col] != 0:
                current_col = col
                while current_col - 1 >= 0 and matt[row][current_col - 1] == 0:
                    matt[row][current_col - 1] = matt[row][current_col]
                    matt[row][current_col] = 0
                    current_col -= 1


def gameRight(matt):
    for row in range(GAME_SIZE):

        for col in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0:
                current_col = col
                while current_col + 1 < GAME_SIZE and matt[row][current_col + 1] == 0:
                    matt[row][current_col + 1] = matt[row][current_col]
                    matt[row][current_col] = 0
                    current_col += 1

        for col in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0 and matt[row][col] == matt[row][col + 1]:
                matt[row][col + 1] *= 2
                matt[row][col] = 0

        for col in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0:
                current_col = col
                while current_col + 1 < GAME_SIZE and matt[row][current_col + 1] == 0:
                    matt[row][current_col + 1] = matt[row][current_col]
                    matt[row][current_col] = 0
                    current_col += 1


def startGame():
    matt = CreateMat()
    firstMove(matt)
    printGame(matt)
    while(True):
        cellNum = getEmptyCellNum(matt)
        insertRandom(matt, cellNum, 0)
        printGame(matt)
        x = input("Enter your next move: ")
        match x:
            case 'down':
                gameDown(matt)
            case 'up':
                gameUp(matt)
            case 'left':
                gameLeft(matt)
            case 'right':
                gameRight(matt)
            case 0:
                return 0

def main():
    matt = [[4, 0, 4, 0],
            [2, 2, 4, 0],
            [2, 0, 4, 0],
            [4, 0, 4, 0]]
    # printGame(matt)
    # gameDown(matt)
    # printGame(matt)
    # gameDown(matt)
    # printGame(matt)
    startGame()

if __name__ == '__main__':
    main()
