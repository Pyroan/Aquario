# Right now is still, but hopefully someday it'll be
# reactive to bubbles + fish food and stuff
import curses

from .entity import Entity


class Water(Entity):
    def __init__(self, y):
        self.y = y

    def update(self, delta_time):
        pass

    def draw(self, stdscr):
        stdscr.hline(self.y, 0, '~', curses.COLS)
