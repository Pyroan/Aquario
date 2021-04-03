# A fish...
import curses
import random
import math
from time import time
from util import Vector2

class Fish:
    IDLE = 1

    def __init__(self, x: int, y: int, reflected: bool):
        self.x = x
        self.y = y
        self.state = self.IDLE
        self.reflected = reflected

    def update(self, delta_time):
        if self.state == self.IDLE:
            pass

    def draw(self, stdscr):
        if not self.reflected:
            stdscr.addstr(self.y, self.x+2, ")\\")
            stdscr.addstr(self.y+1, self.x, ">{|)'>")
            stdscr.addstr(self.y+2, self.x+2, ")/")
        else:
            stdscr.addstr(self.y, self.x+2, "/(")
            stdscr.addstr(self.y+1, self.x, "<'(|}<")
            stdscr.addstr(self.y+2, self.x+2, "\\(")
