import sys

# Windows support is for losers who know how to make curses work.
import curses
from time import time

from bubbler import Bubbler
from water import Water

entities = []


def update():
    t = time()
    delta_time = 1000//15  # let's just pretend framerates aren't a problem

    for e in entities:
        e.update(delta_time)


def draw(stdscr):
    # Clear screen
    stdscr.erase()
    # Draw stuff
    for e in entities:
        e.draw(stdscr)
    # Apply drawing
    stdscr.refresh()


def main(stdscr):
    # Setup
    curses.curs_set(0)
    stdscr.leaveok(True)
    stdscr.timeout(1000//15)

    # Add water
    entities.append(Water(2))
    entities.append(Bubbler(10, 90, 30, 1, 4))
    # Main Loop
    running = True
    while(running):
        update()
        draw(stdscr)

        # Handle input
        c = stdscr.getch()
        if (c > 0):
            running = False


curses.wrapper(main)
