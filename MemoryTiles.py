
'''
GUI implementation of the memory tiles game with the  4x3 square box...
And these are the libraries that are used to implement the following game...
'''

import tkinter as TileGame
import random
from tkinter import messagebox
import time


class MemoryTiles:
    def __init__(self, parent):
        self.parent = parent
        # The height and width of the start window of the game...
        self.buttons = [[TileGame.Button(root, width=4, height=2,
                                         command=lambda row=row, column=column: self.choose_tile(row, column)
                                         ) for column in range(4)] for row in range(4)]
        for row in range(4):
            for column in range(4):
                self.buttons[row][column].grid(row=row, column=column)
        self.first = None
        self.draw_board()

# draw_board function helps to open the window when the main function is called to run...
    def draw_board(self):
        self.answer = list('AABBCCDDEEFFGGHH')  # sample text...
        random.shuffle(self.answer)     # shuffles the answer within the 16 tiles (optional.)
        self.answer = [self.answer[:4],
                       self.answer[4:8],
                       self.answer[8:12],
                       self.answer[12:]]

        for row in self.buttons:
            for button in row:
                button.config(text='', state=TileGame.NORMAL)
        self.start_time = time.monotonic() #timer starts as soon as the user clickes the first tile.

# choose_tile function describes the tiles that has to be shown when the user clicks a specific tile...
    def choose_tile(self, row, column):
        self.buttons[row][column].config(text=self.answer[row][column])
        self.buttons[row][column].config(state=TileGame.DISABLED)
        if not self.first:
            self.first = (row, column)
        else:
            a, b = self.first
            if self.answer[row][column] == self.answer[a][b]:
                self.answer[row][column] = ''
                self.answer[a][b] = ''
                if not any(''.join(row) for row in self.answer):
                    duration = time.monotonic() - self.start_time
                    messagebox.showinfo(title='Success!', message='You win! Time: {:.1f}'.format(duration))
                    self.parent.after(5000, self.draw_board)  # set the value appraring on the tile for 5 sec...
            else:
                self.parent.after(3000, self.hide_tiles, row, column, a,
                                  b)  # window will close after 3 sec after end...
            self.first = None

    def hide_tiles(self, x1, y1, x2, y2):
        self.buttons[x1][y1].config(text='', state=TileGame.NORMAL)
        self.buttons[x2][y2].config(text='', state=TileGame.NORMAL)


# accessing the the root function and inserting the 'root' as the argument in the MemoryTile Class.
root = TileGame.Tk()
memory_tile = MemoryTiles(root)
root.mainloop()  # Runs an infinite loop to keep the window until the user clicks the close the button..
