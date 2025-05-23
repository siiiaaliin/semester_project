from tkinter import *
from tkinter import PhotoImage, messagebox
import random
#код аліни
class GameData:
    def __init__(self, rows=4, cols=4):
        self.rows = rows
        self.cols = cols
        self.total_cells = rows * cols

        file_names = [
            "/Users/alinastratiichuk/Desktop/cat1.png", "/Users/alinastratiichuk/Desktop/cat2.png",
            "/Users/alinastratiichuk/Desktop/cat3.png", "/Users/alinastratiichuk/Desktop/cat4.png",
            "/Users/alinastratiichuk/Desktop/cat5.png", "/Users/alinastratiichuk/Desktop/cat6.png",
            "/Users/alinastratiichuk/Desktop/cat7.png", "/Users/alinastratiichuk/Desktop/cat8.png"
        ]

        self.images = [PhotoImage(file=path) for path in file_names]
        all_images = self.images * 2
        random.shuffle(all_images)

        self.board = []
        index = 0
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(all_images[index])
                index += 1
            self.board.append(row)

        self.revealed = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(False)
            self.revealed.append(row)

    def get_image(self, r, c):
        return self.board[r][c]

    def reveal(self, r, c):
        self.revealed[r][c] = True

    def hide(self, r, c):
        self.revealed[r][c] = False

    def is_revealed(self, r, c):
        return self.revealed[r][c]

    def is_finished(self):
        for row in self.revealed:
            for cell in row:
                if not cell:
                    return False
        return True

# ==== Частина Ангеліни ====
root = Tk()
root.title("Memory Game")

frame = Frame(root)
frame.pack()

ROWS = 4
COLS = 4

game = GameData(rows=ROWS, cols=COLS)
back_img = PhotoImage(file="/Users/alinastratiichuk/Desktop/back.png")

buttons = []
for row in range(ROWS):
    row_buttons = []
    for col in range(COLS):
        btn = Button(frame, width=100, height=100, image=back_img,
                     command=lambda r=row, c=col: on_button_click(r, c))
        btn.grid(row=row, column=col)
        row_buttons.append(btn)
    buttons.append(row_buttons)

# ==== Частина Русі ====
first=None
second=None
click_block=False

def on_button_click(row, col):
    global first, second, click_block

    if game.is_revealed(row, col) or click_block:
        return

    buttons[row][col]["image"] = game.get_image(row, col)

    if first is None:
        first = (row, col)
    elif second is None:
        second = (row, col)
        click_block = True

        r1, c1 = first
        r2, c2 = second

        if game.get_image(r1, c1) == game.get_image(r2, c2):
            game.reveal(r1, c1)
            game.reveal(r2, c2)
            click_block = False
            reset_selection()

            if game.is_finished():
                messagebox.showinfo("Гру завершено", "Вітаємо! Ви відкрили всі пари!")
        else:
            root.after(1000, lambda: hide_pair(r1, c1, r2, c2))

def hide_pair(r1, c1, r2, c2):
    global click_block
    buttons[r1][c1]["image"] = back_img
    buttons[r2][c2]["image"] = back_img
    click_block = False
    reset_selection()

def reset_selection():
    global first, second
    first = None
    second = None

root.mainloop()
