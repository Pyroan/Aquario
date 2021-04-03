# The filter bubbly boy.
# basically just a particle emitter.
import curses
import random
import math
from time import time

from .entity import Entity
from aquario.util import Vector2


class Bubble:
    life = 0
    char = '.'

    # Particles
    def __init__(self, x: int, y: int, offset):
        self.x = x
        self.y = y
        self.size = 1
        self.velocity = Vector2(0, 0)
        self.offset = offset

    # return whether this should be deleted
    def update(self, delta_time):
        # Die on surface
        if self.y <= 2:
            return True
        # Pick character
        if self.life > 2:
            self.char = 'o'
        elif self.life > 5:
            self.char = 'O'
        # Handle movement
        self.velocity.y = -1  # don't worry about it
        # again don't worry about it
        self.velocity.x = math.sin((self.life + self.offset)/(2*math.pi)) / 2
        self.x += self.velocity.x
        self.y += self.velocity.y
        if self.y < 0:
            self.y = 0

        self.life += 1
        return False

    def draw(self, stdscr):
        if 0 < self.x < curses.COLS and 0 < self.y < curses.COLS:
            stdscr.addch(self.y, round(self.x), self.char)


# Particle generator
class Bubbler(Entity):

    def __init__(self, height: int, emit_rate: float):
        self.particles = []
        self.x = 5
        self.y = 0

        self.height = height
        self.emit_rate = emit_rate

    def update(self, delta_time):
        for p in self.particles:
            delete = p.update(delta_time)
            if delete:
                self.particles.remove(p)
        # i'm literally just making this stuff up at this point
        if random.randint(0, 100) < self.emit_rate:
            self.particles.append(
                Bubble(self.x+3, self.y+2+self.height, random.randrange(0, 100)))

    def draw(self, stdscr):
        # Draw top filter thing
        stdscr.hline(self.y, self.x+1, '_', 3)
        stdscr.hline(self.y+1, self.x, '_', 3)
        stdscr.insch(self.y+1, self.x, "|")
        stdscr.insch(self.y+1, self.x+4, "|")
        # Draw stem
        stdscr.vline(self.y+2, self.x+1, '|', self.height)
        stdscr.vline(self.y+2, self.x+2, '|', self.height)
        stdscr.hline(self.y+2+self.height, self.x+1, '#', 2)
        # Draw bubbles
        for p in self.particles:
            p.draw(stdscr)
