import pytest
from maze_generator.generator import Maze, InvalidMazeSize


def test_random_cell_creation():
    maze=Maze(15,15)
    # Border values for 15x15
    maze.set_cell(14,14)
    maze.set_wall(14,14)
    maze.set_cell(14,7)
    maze.set_wall(14,7)
    maze.set_cell(0,6)
    maze.set_wall(0,6)
    #Value for Cell in a center
    maze.set_cell(5,5)
    maze.set_wall(5,5)
    maze_matrix = maze.get_maze()
    assert maze_matrix[14][14] == "c"
    assert maze_matrix[13][14] == "w"
    assert maze_matrix[14][13] == 'w'
    assert maze_matrix[14][6] == "w"
    assert maze_matrix[14][8] == "w"
    assert maze_matrix[13][7] == "w"
    assert maze_matrix[0][5] == "w"
    assert maze_matrix[0][7] == "w"
    assert maze_matrix[1][6] == "w"
    assert maze_matrix[4][5] == "w"
    assert maze_matrix[5][6] == "w"
    assert maze_matrix[5][4] == "w"
    assert maze_matrix[6][5] == "w"

def test_invalid_maze_user_input():
    with pytest.raises(TypeError):
        Maze("dlada","dada")
        Maze("32",16)
        Maze(323.32,32.4)




