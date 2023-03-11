import random
from typing import List
import numpy as np
from exceptions import InvalidMazeSize
import logging
import time

# Initializing Matrix return List[list]
def init_maze(width:int=10 , height:int=10):
    maze = [['u']*height]*width
    return maze

# Printing Maze
def print_maze(maze: List[list]):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j],end=" ")
        print()

def maze_generator(maze):
    #TODO
    # u-unvisited  c-cell  w-wall
    return maze

def main():
    try:
        user_input = list(map(int,(input("Give Width and Height: ").split())))
        if user_input[0] > 18 or user_input[1] > 18:
            raise InvalidMazeSize(user_input[0],user_input[1])
        maze = init_maze(user_input[0], user_input[1])

    except ValueError:
        logging.error(f" Width and Height must be a INTEGER")
        logging.warning(f" Initializing Maze With default Values 10-Width 10-Height")
        time.sleep(0.5)
        maze = init_maze()

    print("\nMaze Correctly Initialized\n")
    print_maze(maze)

if __name__ == "__main__":
    main()