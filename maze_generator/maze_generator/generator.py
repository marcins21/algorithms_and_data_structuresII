import random
from typing import List

import numpy as np

from exceptions import InvalidMazeSize
import logging
import time
from colorama import init, Fore

class Maze:
    def __init__(self,width:int=10,height:int=10):
        self.maze = np.full((height,width),"u")
        self.width = width
        self.height = height

    def get_maze(self):
        return self.maze
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width

    def set_cell(self,h:int,w:int):
        self.maze[h][w] = "c"
        
    def set_wall(self,h:int, w:int):
        if w+1 < self.width:
            self.maze[h][w+1] = "w"
        if w-1 >= 0:
            self.maze[h][w-1] = "w"
        if h+1 < self.width:
            self.maze[h+1][w] = "w"
        if h-1 >= 0:
            self.maze[h-1][w] = "w"


# Printing Maze
def print_maze(maze):
    maze_list = maze.get_maze()
    for i in range(len(maze_list)):
        for j in range(len(maze_list[0])):
            if maze_list[i][j] == "u":
                print(Fore.WHITE,f"{maze_list[i][j]}",end=" ")
            elif maze_list[i][j] == "c":

                print(Fore.GREEN, f"{maze_list[i][j]}", end=" ")
            else:
                print(Fore.RED, f"{maze_list[i][j]}", end=" ")
        print()

def maze_generator(maze,width,height):
    # TODO
    # u-unvisited  c-cell  w-wall
    start_width = random.randint(0,width-1)
    start_height = random.randint(0,height-1)

    #Debug info
    print(start_width,start_height)

    maze.set_cell(start_height,start_width)
    maze.set_wall(start_height,start_width)


    return maze

def main():
    try:
        user_input = list(map(int,(input("Give Width and Height: ").split())))
        if user_input[0] > 18 or user_input[1] > 18:
            raise InvalidMazeSize(user_input[0],user_input[1])
        maze = Maze(user_input[0], user_input[1])

    except ValueError:
        logging.error(f" Width and Height must be a INTEGER")
        logging.warning(f" Initializing Maze With default Values 10-Width 10-Height")
        time.sleep(0.5)
        maze = Maze()


    print("\nMaze Correctly Initialized\n")
    print_maze(maze)

    print(f"\nGenerated!")
    new_maze = maze_generator(maze,maze.get_width(),maze.get_height())
    print_maze(new_maze)


if __name__ == "__main__":
    main()