from tkinter import *
from tkinter import PhotoImage
import random

class GameData:
    def __init__(self, rows=4, cols=4):
        self.rows=rows
        self.cols=cols
        self.total_cells=rows*cols

        file_names=["/Users/alinastratiichuk/Desktop/cat1.png", "/Users/alinastratiichuk/Desktop/cat2.png", "/Users/alinastratiichuk/Desktop/cat3.png", "/Users/alinastratiichuk/Desktop/cat4.png","/Users/alinastratiichuk/Desktop/cat5.png", "/Users/alinastratiichuk/Desktop/cat6.png", "/Users/alinastratiichuk/Desktop/cat7.png", "/Users/alinastratiichuk/Desktop/cat8.png"]
        self.images=[]
        for path in file_names:
            img=PhotoImage(file=path)
            self.images.append(img)

        all_images=self.images*2
        random.shuffle(all_images)

        self.board=[]
        index=0
        for i in range(self.rows):
            row=[]
            for j in range(self.cols):
                row.append(all_images[index])
                index+=1
            self.board.append(row)

        self.revealed = [] #всі картинки закриті спочатку
        for i in range(self.rows):
            row=[]
            for j in range(self.cols):
                row.append(False)
            self.revealed.append(row)

    def get_image(self, r, c):
        return self.board[r][c]

    def reveal(self, r, c): #позначає як відкриту
        self.revealed[r][c]=True

    def hide(self, r, c): #ховає картинку, якщо не співпадає
        self.revealed[r][c]=False

    def is_revealed(self, r, c):
        return self.revealed[r][c]

    def is_finished(self): #допоміжна функція
        for row in self.revealed:
            for cell in row:
                if not cell:
                    return False  # якщо хоч одна клітинка закрита — гра не завершена
        return True  # якщо жодна не закрита — гра завершена

#частина ангеліни
root = Tk()
root.title("Memory Game")  

frame = Frame(root)  
frame.pack()  

ROWS = 4
COLS = 4 #поле задаю параметр

game=GameData(rows=ROWS, cols=COLS) #додала я
back_img=PhotoImage(file="/Users/alinastratiichuk/Desktop/back.png") #додала я

buttons = []

for row in range(ROWS):
    row_buttons = []  
    for col in range(COLS):
        
        btn = Button(frame,        
                     width=100, height=100, #і тут дещо додала і прибрала
                     image=back_img,    
                     command=lambda r=row, c=col: on_button_click(r, c))  
        btn.grid(row=row, column=col)  
        row_buttons.append(btn)  
    buttons.append(row_buttons)

def on_button_click(row, col):
    
    btn = buttons[row][col]  
    btn["image"] = game.get_image(row, col)         # ЗМІНИЛА

root.mainloop()
