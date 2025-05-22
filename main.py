from tkinter import *  

root = Tk()
root.title("Memory Game")  

frame = Frame(root)  
frame.pack()  

ROWS = 4
COLS = 4 #поле задаю параметр


buttons = []

for row in range(ROWS):
    row_buttons = []  
    for col in range(COLS):
        
        btn = Button(frame,
                     text="",      #поки порожній          
                     width=18, height=9,      
                     command=lambda r=row, c=col: on_button_click(r, c))  
        btn.grid(row=row, column=col)  
        row_buttons.append(btn)  
    buttons.append(row_buttons)

def on_button_click(row, col):
    
    btn = buttons[row][col]  
    btn["text"] = "поки без картинки :("        # імітація відкриття картинки

root.mainloop()
