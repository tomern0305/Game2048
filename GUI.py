import random
import tkinter as tk

# from PIL import Image, ImageTk

GAME_SIZE = 4


def CreateMat():
    matt = []
    for i in range(GAME_SIZE):
        matt.append([0] * GAME_SIZE)
    return matt


def getEmptyCellNum(matt):
    cells = []
    for i in range(GAME_SIZE):
        for j in range(GAME_SIZE):
            if matt[i][j] == 0:
                cells.append([i, j])
    return random.choice(cells) if cells else None


def getNumOfEmptyCells(matt):
    count = 0
    for i in range(GAME_SIZE):
        for j in range(GAME_SIZE):
            if matt[i][j] == 0:
                count += 1
    return count


def insertRandom(matt):
    cellNum = getEmptyCellNum(matt)
    if cellNum:
        bank = [2, 2, 4]
        matt[cellNum[0]][cellNum[1]] = random.choice(bank)

def findMax(matt):
    return max(max(row) for row in matt)

def get_color(value):
    # Example color scheme based on tile value
    colors = {0: "lightgrey", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
              16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
              256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
    return colors.get(value, "#3c3a32")


# Move functions (Up, Down, Left, Right) remain the same as in your current code
def update_grid():
    for i in range(GAME_SIZE):
        for j in range(GAME_SIZE):
            value = matt[i][j]
            tile_labels[i][j].config(text=str(value) if value != 0 else "", bg=get_color(value))


# Start the game and initialize Tkinter interface
def startGame():
    global matt
    matt = CreateMat()
    insertRandom(matt)
    insertRandom(matt)
    update_grid()

    game_over_label.config(text="")
    game_over_label.place_forget()


def gameDown(matt):
    state = False
    for col in range(GAME_SIZE):
        for row in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0:
                current_row = row
                while current_row + 1 < GAME_SIZE and matt[current_row + 1][col] == 0:
                    matt[current_row + 1][col] = matt[current_row][col]
                    matt[current_row][col] = 0
                    current_row += 1
                    state = True

        for row in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0 and matt[row][col] == matt[row + 1][col]:
                matt[row + 1][col] *= 2
                matt[row][col] = 0
                state = True

        for row in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0:
                current_row = row
                while current_row + 1 < GAME_SIZE and matt[current_row + 1][col] == 0:
                    matt[current_row + 1][col] = matt[current_row][col]
                    matt[current_row][col] = 0
                    current_row += 1
    return state


def gameCheckDown(matt):
    for col in range(GAME_SIZE):
        for row in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0:
                current_row = row
                while current_row + 1 < GAME_SIZE and matt[current_row + 1][col] == 0:
                    # matt[current_row + 1][col] = matt[current_row][col]
                    # matt[current_row][col] = 0
                    # current_row += 1
                    return False

        for row in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0 and matt[row][col] == matt[row + 1][col]:
                # matt[row + 1][col] *= 2
                # matt[row][col] = 0
                return False

        for row in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0:
                current_row = row
                while current_row + 1 < GAME_SIZE and matt[current_row + 1][col] == 0:
                    # matt[current_row + 1][col] = matt[current_row][col]
                    # matt[current_row][col] = 0
                    # current_row += 1
                    return False
    return True


def gameUp(matt):
    state = False
    for col in range(GAME_SIZE):
        for row in range(1, GAME_SIZE):
            if matt[row][col] != 0:
                current_row = row
                while current_row - 1 >= 0 and matt[current_row - 1][col] == 0:
                    matt[current_row - 1][col] = matt[current_row][col]
                    matt[current_row][col] = 0
                    current_row -= 1
                    state = True

        for row in range(1, GAME_SIZE):
            if matt[row][col] != 0 and matt[row][col] == matt[row - 1][col]:
                matt[row - 1][col] *= 2
                matt[row][col] = 0
                state = True

        for row in range(1, GAME_SIZE):
            if matt[row][col] != 0:
                current_row = row
                while current_row - 1 >= 0 and matt[current_row - 1][col] == 0:
                    matt[current_row - 1][col] = matt[current_row][col]
                    matt[current_row][col] = 0
                    current_row -= 1
    return state


def gameCheckUp(matt):
    for col in range(GAME_SIZE):
        for row in range(1, GAME_SIZE):
            if matt[row][col] != 0:
                current_row = row
                while current_row - 1 >= 0 and matt[current_row - 1][col] == 0:
                    # matt[current_row - 1][col] = matt[current_row][col]
                    # matt[current_row][col] = 0
                    # current_row -= 1
                    return False

        for row in range(1, GAME_SIZE):
            if matt[row][col] != 0 and matt[row][col] == matt[row - 1][col]:
                # matt[row - 1][col] *= 2
                # matt[row][col] = 0
                state = False

        for row in range(1, GAME_SIZE):
            if matt[row][col] != 0:
                current_row = row
                while current_row - 1 >= 0 and matt[current_row - 1][col] == 0:
                    # matt[current_row - 1][col] = matt[current_row][col]
                    # matt[current_row][col] = 0
                    # current_row -= 1
                    return False
    return True


def gameLeft(matt):
    state = False
    for row in range(GAME_SIZE):
        for col in range(1, GAME_SIZE):
            if matt[row][col] != 0:
                current_col = col
                while current_col - 1 >= 0 and matt[row][current_col - 1] == 0:
                    matt[row][current_col - 1] = matt[row][current_col]
                    matt[row][current_col] = 0
                    current_col -= 1
                    state = True

        for col in range(1, GAME_SIZE):
            if matt[row][col] != 0 and matt[row][col] == matt[row][col - 1]:
                matt[row][col - 1] *= 2
                matt[row][col] = 0
                state = True

        for col in range(1, GAME_SIZE):
            if matt[row][col] != 0:
                current_col = col
                while current_col - 1 >= 0 and matt[row][current_col - 1] == 0:
                    matt[row][current_col - 1] = matt[row][current_col]
                    matt[row][current_col] = 0
                    current_col -= 1
    return state


def gameCheckLeft(matt):
    for row in range(GAME_SIZE):
        for col in range(1, GAME_SIZE):
            if matt[row][col] != 0:
                current_col = col
                while current_col - 1 >= 0 and matt[row][current_col - 1] == 0:
                    # matt[row][current_col - 1] = matt[row][current_col]
                    # matt[row][current_col] = 0
                    # current_col -= 1
                    return False

        for col in range(1, GAME_SIZE):
            if matt[row][col] != 0 and matt[row][col] == matt[row][col - 1]:
                # matt[row][col - 1] *= 2
                # matt[row][col] = 0
                return False

        for col in range(1, GAME_SIZE):
            if matt[row][col] != 0:
                current_col = col
                while current_col - 1 >= 0 and matt[row][current_col - 1] == 0:
                    # matt[row][current_col - 1] = matt[row][current_col]
                    # matt[row][current_col] = 0
                    # current_col -= 1
                    return False
    return True


def gameRight(matt):
    state = False
    for row in range(GAME_SIZE):
        for col in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0:
                current_col = col
                while current_col + 1 < GAME_SIZE and matt[row][current_col + 1] == 0:
                    matt[row][current_col + 1] = matt[row][current_col]
                    matt[row][current_col] = 0
                    current_col += 1
                    state = True

        for col in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0 and matt[row][col] == matt[row][col + 1]:
                matt[row][col + 1] *= 2
                matt[row][col] = 0
                state = True

        for col in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0:
                current_col = col
                while current_col + 1 < GAME_SIZE and matt[row][current_col + 1] == 0:
                    matt[row][current_col + 1] = matt[row][current_col]
                    matt[row][current_col] = 0
                    current_col += 1
    return state


def gameCheckRight(matt):
    for row in range(GAME_SIZE):
        for col in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0:
                current_col = col
                while current_col + 1 < GAME_SIZE and matt[row][current_col + 1] == 0:
                    # matt[row][current_col + 1] = matt[row][current_col]
                    # matt[row][current_col] = 0
                    # current_col += 1
                    return False

        for col in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0 and matt[row][col] == matt[row][col + 1]:
                # matt[row][col + 1] *= 2
                # matt[row][col] = 0
                return False

        for col in range(GAME_SIZE - 2, -1, -1):
            if matt[row][col] != 0:
                current_col = col
                while current_col + 1 < GAME_SIZE and matt[row][current_col + 1] == 0:
                    # matt[row][current_col + 1] = matt[row][current_col]
                    # matt[row][current_col] = 0
                    # current_col += 1
                    return False
    return True


def checkEndGame(matt):
    if gameCheckDown(matt) and gameCheckUp(matt) and gameCheckLeft(matt) and gameCheckRight(matt):
        for i in range(GAME_SIZE):
            for j in range(GAME_SIZE):
                value = matt[i][j]
                tile_labels[i][j].config(text=str(value) if value != 0 else "", bg=get_color("lightgrey"))
        # label = tk.Label(root, text="Game Over")
        # label.pack(padx=5, pady=5)

        game_over_label.config(text="Game Over", fg="black", font=("Arial", 36, "bold"))
        game_over_label.place(relx=0.5, rely=0.5, anchor="center")


# title
root = tk.Tk()
root.title("2048")

root.geometry("400x400")

# logo
# path = "2048_logo.png"
# load = Image.open(path)
# render = ImageTk.PhotoImage(load)
# root.iconphoto(False, render)

# label = tk.Label(root, text="Welcome to 2048!")
# label.pack(padx=5, pady=5)

button = tk.Button(root, text="Restart", command=startGame)
button.pack(padx=5, pady=5)

frame = tk.Frame(root)
frame.pack()

game_over_label = tk.Label(root, text="", fg="red", font=("Arial", 36, "bold"))

# Create grid of labels for displaying the game matrix
tile_labels = [[None for _ in range(GAME_SIZE)] for _ in range(GAME_SIZE)]

for i in range(GAME_SIZE):
    for j in range(GAME_SIZE):
        label = tk.Label(frame, text="", width=4, height=2, font=("Arial", 24), bg="lightgrey", borderwidth=2, relief="solid")
        label.grid(row=i, column=j, padx=5, pady=5)
        tile_labels[i][j] = label





# Handle key events for movement
def key_handler(event):
    state = False
    if event.keysym == "Up":
        state = gameUp(matt)
    elif event.keysym == "Down":
        state = gameDown(matt)
    elif event.keysym == "Left":
        state = gameLeft(matt)
    elif event.keysym == "Right":
        state = gameRight(matt)

    if getNumOfEmptyCells(matt) == 0:
        res = checkEndGame(matt)


    if state:
        insertRandom(matt)
        update_grid()

# Bind the key events to the game logic
root.bind("<Up>", key_handler)
root.bind("<Down>", key_handler)
root.bind("<Left>", key_handler)
root.bind("<Right>", key_handler)

# Start the game
startGame()

# Run Tkinter main loop
root.mainloop()
