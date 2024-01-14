from tkinter import *
from random import randint

numbers_str = [["0" for _ in range(5)]for _ in range(5)]
buttons = [[None]*5 for _ in range(5)]
numbers = [[None]*5 for _ in range(5)]
BINGO = 0

def convert_to_int(_2dlist):
    list = [[None]*5 for _ in range(5)]
    for i in range(len(_2dlist)):
        for j in range(len(_2dlist[i])):
            list[i][j] = int(_2dlist[i][j])
    return list

temp = 1
for i in range(5):
    for j in range(5):
        if( len(str(temp)) == 1):
            numbers_str[i][j] = f'0{temp}'
        else:
            numbers_str[i][j] = f'{temp}'
        temp = temp+1;

def rand():
    if not any(numbers_str[i][j] for i in range(5) for j in range(5)):
        return
    
    while True:
        i, j = randint(0, 4), randint(0, 4)
        if numbers_str[i][j] != 0:
            break

    x = numbers_str[i][j]
    numbers_str[i][j] = 0
    return x

def checkWin(row, col):
    global BINGO
    row_done = True
    for j in range(5):
        if numbers[row][j] != 0:
            row_done = False
            break
    if row_done:
        BINGO += 1

    col_done = True
    for i in range(5):
        if numbers[i][col] != 0:
            col_done = False
            break
    if col_done:
        BINGO += 1

    diag_done = True
    if row == col:
        for i in range(5):
            if numbers[i][i] != 0:
                diag_done = False
                break
        if diag_done:
            BINGO += 1

    anti_diag_done = True
    if row + col == 4:
        for i in range(5):
            if numbers[i][4 - i] != 0:
                anti_diag_done = False
                break
        if anti_diag_done:
            BINGO += 1
    if BINGO == 5:
        win_label.config(text="Congratulations! You've won the game!", font=("Helvetica", 20, "bold"), fg="green")
        return

def button_click(row, col):
    buttons[row][col].config(bg="black",fg="white",state=DISABLED)
    numbers[row][col] = 0
    checkWin(row,col)

main = Tk()

win_label = Label(main, text="", font=("Helvetica", 5))
win_label.grid(row=6, column=0,columnspan=5)

for i in range(5):
    for j in range(5):
        temp = rand()
        cell = Button(main, text=temp,font=("Comic Sans",30),padx=2,pady=2,command=lambda row=i, col=j:button_click(row, col))
        cell.grid(row=i,column=j)

        buttons[i][j] = cell
        numbers[i][j] = int(temp)

main.mainloop()