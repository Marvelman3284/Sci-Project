from maze_utils import generate_maze, show_maze_and_solution

# dimensions of the maze
# must be odd-numbered
# includes outer walls
dimensions = [49, 81]

# creates maze of above dimensions
# check whether a cell is a wall like:
#     maze[30, 40] == WALL
# this also works as expected:
#     maze[20, 7] == PATH
maze = generate_maze(dimensions)

# your code should fill this list with [x, y] pairs of
# all of the cells along your proposed solution path
solution = []




#########################################
### YOUR CODE TO SOLVE MAZE GOES HERE ###
#########################################






# this will display the maze
# the points along your solution path withh be highlighted in yellow
# if they are highlighted in red, your path goes through a wall!
show_maze_and_solution(maze, solution)
