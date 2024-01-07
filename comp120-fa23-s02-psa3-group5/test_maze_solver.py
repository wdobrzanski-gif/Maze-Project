"""
Module: test_maze_solver

pytest module for the maze_solver function.
"""

import pytest

from maze_solver import maze_solver, Maze
from agenda import StackAgenda, QueueAgenda

def test_maze1():
    m = Maze('tester_maze1.txt')

    # test that we get the correct result with the stack agenda
    sa = StackAgenda()
    result = maze_solver(m, sa, wait_for_user=False)
    assert result == True

    # test that we get the correct result with the queue agenda
    m = Maze('tester_maze1.txt') # create a new maze since the old one was changed by maze_solver

    qa = QueueAgenda()
    result = maze_solver(m, qa, wait_for_user=False)
    assert result == True

# TODO: add test cases for each of the tester_mazeX.txt files (one test
# case/function per maze file)


# DO NOT change anything below this line
if __name__ == "__main__":
    pytest.main(['test_maze_solver.py'])
