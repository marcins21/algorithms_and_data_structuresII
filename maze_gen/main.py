import pygame
import random
import time

# Maze dimensions
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20

# Maze grid size
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Colors

WHITE = (255, 255, 255)
COLOR = (235, 200, 150)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Initialize the maze grid
grid = [[True] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
stack = [(0, 0)]

# Generate the maze using depth-first search
while stack:
    current_cell = stack[-1]
    x, y = current_cell

    # Mark the current cell as visited
    grid[y][x] = False

    # Get neighbors of the current cell
    neighbors = []
    if x > 1 and grid[y][x - 2]:
        neighbors.append((x - 2, y))
    if x < GRID_WIDTH - 2 and grid[y][x + 2]:
        neighbors.append((x + 2, y))
    if y > 1 and grid[y - 2][x]:
        neighbors.append((x, y - 2))
    if y < GRID_HEIGHT - 2 and grid[y + 2][x]:
        neighbors.append((x, y + 2))

    if neighbors:
        # Choose a random neighbor
        next_x, next_y = random.choice(neighbors)

        # Remove the wall between the current cell and the chosen neighbor
        if next_x < x:
            grid[y][x - 1] = False
        elif next_x > x:
            grid[y][x + 1] = False
        elif next_y < y:
            grid[y - 1][x] = False
        elif next_y > y:
            grid[y + 1][x] = False

        # Push the chosen neighbor to the stack
        stack.append((next_x, next_y))

    else:
        # Backtrack if no unvisited neighbors
        stack.pop()

# Game loop
running = True
index = 0  # Index to track the current step of visualization
revealed_grid = [[False] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Update revealed grid
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if x <= index % GRID_WIDTH and y <= index // GRID_WIDTH:
                revealed_grid[y][x] = True

    # Draw the maze up to the current step
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x]:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif revealed_grid[y][x]:
                pygame.draw.rect(screen, COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Increment index to move to the next step
    index += 1

    # If all steps are done, exit the loop
    if index >= GRID_WIDTH * GRID_HEIGHT:
        break

    pygame.display.flip()
    clock.tick(60)
    time.sleep(0.001)

pygame.quit()

