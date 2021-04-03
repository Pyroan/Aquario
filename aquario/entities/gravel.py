import curses
from random import randint

from .entity import Entity

class Gravel(Entity):
    

    def __init__(self, height, density):
        self.x = 0
        self.y = curses.LINES - height

        self.sprite = '\n'.join([''.join([('oO'+' '*density*n)[randint(0,density*n+1)] for _ in range(curses.COLS-1)]) for n in range(height)])


    def update(self, delta_time):
        pass

    def draw(self, stdscr):
        stdscr.addstr(self.y ,self.x, self.sprite)
