import curses
from random import randint

from .entity import Entity

class Gravel(Entity):
    

    def __init__(self):
        self.x = 0
        self.y = curses.LINES - 5

        self.sprite = '\n'.join([''.join([('oO'+' '*9*n)[randint(0,9*n+1)] for _ in range(curses.COLS-1)]) for n in range(5)])


    def update(self, delta_time):
        pass

    def draw(self, stdscr):
        stdscr.addstr(self.y ,self.x, self.sprite)
