# A fish...
import curses
import random
import math
from time import time

from aquario.config import CONFIG
from aquario.util import Vector2, reflected
from .entity import Entity

class Fish(Entity):
    IDLE = 1

    def __init__(self, x: int, y: int, reflected: bool):
        self.x = x
        self.y = y
        self.state = self.IDLE
        self.reflected = reflected

        with open(CONFIG.assets_folder + "fish" + str(random.randint(1,2)) + ".txt") as f:
            self.sprite = []
            for line in f.readlines():
                self.sprite.append(line.strip('\n'))

    def update(self, delta_time):
        if self.state == self.IDLE:
            pass

    def draw(self, stdscr):
        for i in range(len(self.sprite)):

            if not self.reflected:
                stdscr.addstr(self.y+i, self.x, self.sprite[i])
            else:
                stdscr.addstr(self.y+i, self.x, reflected(self.sprite[i]))