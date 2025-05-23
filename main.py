from tkinter import *  

root = Tk()
root.title("Memory Game")  
root.configure(bg="lightpink")

label = Label(root, text="Memory Game", 
              font=("Times New Romans", 16), bg="lightpink")
label.pack(pady=10)

frame = Frame(root, bg="lightblue")  
frame.pack()  

ROWS = 4
COLS = 4 #поле задаю параметр

game=GameData(rows=ROWS, cols=COLS) 
back_img=PhotoImage(file="/Users/alinastratiichuk/Desktop/back.png") 

buttons = []

for row in range(ROWS):
    row_buttons = []  
    for col in range(COLS):
        
        btn = Button(frame,
                     text="",      #поки порожній          
                     width=100, height=100,      
                     image=back_img,
                     command=lambda r=row, c=col: on_button_click(r, c))  
        btn.grid(row=row, column=col,padx=2, pady=2)  
        row_buttons.append(btn)  
    buttons.append(row_buttons)

def on_button_click(row, col):
    
    btn = buttons[row][col]  
    btn["image"] = game.get_image(row, col)       

exit_button = Button(root, text="Вийти", font=("Times New Romans", 16), 
                     command=root.destroy)
exit_button.pack(pady=15)

root.mainloop()
