# Sample code no need to execute...!!!

# GUI code Pth...
'''
import random
import tkinter as tk
from datetime import time
from tkinter import messagebox


class MemoryTile:
    def __int__(self, parent):
        self.parent = parent
        self.buttons = [[tk.Button(root,
                                   width=4,
                                   height=2,
                                   command=lambda row=row, column=column: self.choose_tile(row, column)
                                   ) for column in range(4)] for row in range(4)]
        for row in range(4):
            for column in range(4):
                self.buttons[row][column].grid(row=row, column=column)
        self.first = None
        self.draw_board()

    def generate_board(self):
        self.answer = list('AABBCCDDEEFFGGHH')
        random.shuffle(self.answer)
        self.answer = [self.answer[:4],
                       self.answer[4:8],
                       self.answer[8:12],
                       self.answer[12:]]

        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL)
        self.start_time = time.monotonic()

    def choose_tile(self, row, column):
        self.buttons[row][column].config(text=self.answer[row][column])
        self.buttons[row][column].config(state=tk.DISABLED)
        if not self.first:
            self.first = self.answer[row][column]
        else:
            a, b = self.first
            if self.answer[row][column] == self.answer[a][b]:
                self.answer[row][column] = ''
                self.answer[a][b] = ''
                if not any(''.join(row) for row in self.answer):
                    duration = time.monotonic() - self.start_time
                    messagebox.showinfo(title='Success', message='You win! Time: {:.1f}'.format())
                    self.parent.after(5000, self.draw_board)
            else:
                self.parent.after(3000, self.hide_tiles, row, column, a, b)
            self.first = None

    def hide_tiles(self, x1, y1, x2, y2):
        self.buttons[x1][y1].config(text='', state=tk.NORMAL)
        self.buttons[x2][y2].config(text='', state=tk.NORMAL)


root = tk.Tk()
memory_tile = MemoryTile(root)
root.mainloop()
'''

# Console code

'''
import random
import time

answer = list('AABBCCDDEEFFGGHH')
random.shuffle(answer)
answer = [answer[:4],
         answer[4:8],
         answer[8:12],
         answer[12:]]
board = [list('*'*4) for i in range(4)]

def choose():
    a,b = map(int, input('? '))
    show_board((a,b))
    x,y = map(int, input('? '))
    show_board((a,b),(x,y))
    if answer[a][b] == answer[x][y]:
        print('Matched!')
        board[a][b] = answer[a][b]
        board[x][y] = answer[x][y]
    else:
        print('Not a match.')
    if any('*' in row for row in board):
        return True

def show_board(*tiles):
    for row in range(len(answer)):
        for column in range(len(answer[0])):
            if (row,column) in tiles:
                print(answer[row][column].lower(), end='', flush=True)
            else:
                print(board[row][column], end='', flush=True)
        print()

show_board()
t = time.monotonic()
while choose():
    pass

print('Done! Time:', time.monotonic()-t)

'''
