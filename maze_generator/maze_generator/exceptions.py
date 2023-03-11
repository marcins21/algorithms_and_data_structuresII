import time
# Raises Exception when maze size > 18
class InvalidMazeSize(Exception):
    def __init__(self,maze_size_width,maze_size_heigh):
        self.maze_size_width = maze_size_width
        self.maze_size_height = maze_size_heigh
        self.message = f"\nEXCEPTION - Maze Size is too big {self.maze_size_width}," \
                       f"{maze_size_heigh} declare size below 18"
        super().__init__(self.message)

