import random
import numpy as np
from exceptions import InvalidMazeSize
import logging
import time
from colorama import  Fore

class Maze:
    def __init__(self,width:int=10,height:int=10):
        self.starting_height = None
        self.starting_width = None
        self.maze = np.full((height,width),"u")
        self.width = width
        self.height = height
        self.wall_dict = {}

    def get_maze(self):
        return self.maze
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width

    def set_cell(self,h:int,w:int):
        self.maze[h][w] = "c"

    def set_wall(self,h:int, w:int):
        if w+1 < self.width and self.maze[h][w+1] != "c":
            self.maze[h][w+1] = "w"
        if w-1 >= 0 and self.maze[h][w-1] != "c":
            self.maze[h][w-1] = "w"
        if h+1 < self.width and self.maze[h+1][w] != "c":
            self.maze[h+1][w] = "w"
        if h-1 >= 0 and self.maze[h-1][w] != "c":
            self.maze[h-1][w] = "w"

    def check_neighbors(self,h:int,w:int):
        walls = []
        if w-1 >= 0:
            if self.maze[h][w-1] == "w":
                walls.append([h,w-1])

        if w+1 < self.width:
            if self.maze[h][w+1] == "w":
                walls.append([h,w+1])

        if h+1 < self.height:
           if self.maze[h+1][w] == "w":
               walls.append([h+1,w])

        # Algorytm Nie Przegląda komorek DO GÓRY - idzie tylko w dól BFS
        # Odkomentowanie tych linijek umozliwia przeglądanie takze w górę
        # NIE GWARANTUJE WYJSCIA Z LABIRYNTU, ale zageszcza labirynt

        #
        # if h-1 > 0 and w+1 < self.width:
        #     if self.maze[h-1][w+1] == "w":
        #         walls.append([h-1,w+1])
        #
        # if h-1 > 0 and w-1 >= 0:
        #     if self.maze[h-1][w-1] == "w":
        #         walls.append([h-1,w-1])

        self.wall_dict[(h,w)] = walls

    def randomize_next_move(self,h:int,w:int):
        point_walls = self.wall_dict[(h,w)]

        if not point_walls:
            #print("Returning")
            return

        random_wall_choice = random.choice(point_walls)
        return random_wall_choice

    def get_starting_point(self,sh,sw):
        self.starting_height = sh
        self.starting_width = sw

    def fix_finish(self):
        index_dict = {}
        counter=0
        for i in range(self.width-1):
            if self.maze[self.width-1][i] == "c":
                counter+=1
                index_dict[counter] = i
                self.maze[self.width-1][i] = "w"

        self.maze[self.width-1][index_dict[counter]] = "c"
        new_finish_line = np.char.replace(''.join(self.maze[self.width-1][::]),"c","w",count=counter-1)

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

def maze_generator(maze,height,width):
    # TODO
    # u-unvisited  c-cell  w-wall
    start_width = random.randint(0,width-1)
    start_height = 0
    store_sph = start_height
    store_spw = start_width
    maze.get_starting_point(start_height,start_width)

    #DEBUG INFO
    #print(f"Cell generated {start_height,start_width}")

    #STARTING POINT
    maze.set_cell(start_height,start_width)
    maze.set_wall(start_height,start_width)
    maze.check_neighbors(start_height,start_width)
    next_move = maze.randomize_next_move(start_height, start_width)

    #iterating to maze exit
    runs = []
    while maze.get_height()-2 >= start_height:
        maze.check_neighbors(start_height,start_width)
        next_move = maze.randomize_next_move(start_height, start_width)

        if next_move is None:
            #print("breaking")
            break

        start_height = next_move[0]
        start_width = next_move[1]

        maze.set_cell(next_move[0],next_move[1])
        maze.set_wall(next_move[0],next_move[1])
        runs.append([start_height, start_width])

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

    for i in range(15):
        #DEBUG INFO
        #print("\nMaze Correctly Initialized\n")
        #print_maze(maze)

        #print(f"\nGenerated!")
        new_maze = maze_generator(maze,maze.get_height(),maze.get_width())

    maze.fix_finish()
    print_maze(new_maze)


if __name__ == "__main__":
    main()