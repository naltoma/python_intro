'''A simple maze generator with some **BUGS**

There are many kinds of algorithms for maze[1].
This module supports a maze generator with a simplified depth-first search algorithm[2] below.

step 1: Create a 2-dimensional list by init_maze().
step 2: Set the start point.
step 3: Set the direction at random to dig by set_direction().
step 4: Check the validation the current location to the direction with 2 spaces by is_space().
step 5: If valid, then dig the direction by dig_maze() and back to step 3.

[1] Maze generation algorithm, http://en.m.wikipedia.org/wiki/Maze_generation_algorithm
[2] Depth-First Search, Maze Algorithm, http://www.migapro.com/depth-first-search/
'''

import random

def init_maze(height, width):
    '''ready for non-spaced (all blocked) maze
    All values are set to 0, it means "block".

    Args:
    :param height (int): the height of maze
    :param width (int): the width of maze

    Returns:
    :return: maze (int[][]): double list using as a 2-dimensional maze

    >>> maze = init_maze(3, 2)
    >>> print(maze)
    [[0, 0], [0, 0], [0, 0]]
    '''
    maze = []
    for h in range(height):
        line = []
        for w in range(width):
            line.append(0)
        maze.append(line[:])
    return maze

def print_maze(maze):
    '''print the maze with 2-dimensional map
    Note:
      position "(x, y) = (0, 0)" is set to the upper left on the maze (== maze[0][0]).
      same as position (1, 2) => maze[1][2].

    Args:
    :param maze (int[][]): created by init_maze()

    Returns:
    :return: None

    >>> maze = init_maze(3, 4)
    >>> print_maze(maze)
    ----
    0000
    0000
    0000
    '''
    print('----')
    for line in maze:
        temp = ''
        for value in line:
            temp += str(value)
        print(temp)

def dig_maze(maze, current_x, current_y, diff_x, diff_y):
    '''dig spaces from the current location to target location
    After digging, the spaces are set to 1 when the space are block.

    Args:
    :param maze (int[][]): created by init_maze()
    :param current_x (int): current location in the maze
    :param current_y (int): current location in the maze
    :param diff_x (int): difference between current_x and target_x. (target_x = current_x + diff_x)
    :param diff_y (int): difference between current_y and target_y. (target_y = current_y + diff_y)

    Returns:
    :return: next_x (int): location after digging
    :return: next_y (int): location after digging

    # example code: start at (0, 0), and dig the maze to (2, 0)
    >>> maze = init_maze(3, 4)
    >>> next_x, next_y = dig_maze(maze, 0, 0, 2, 0)
    >>> print_maze(maze)
    ----
    0110
    0000
    0000
    >>> print(next_x, next_y)
    2 0
    '''
    height = len(maze)
    width = len(maze[0])
    if diff_x > 0:
        if current_x + diff_x < width:
            for i in range(diff_x):
                if maze[current_y][current_x + i + 1] == 0:
                    maze[current_y][current_x + i + 1] = 1
    elif diff_x < 0:
        if current_x + diff_x >= 0:
            for i in range(abs(diff_x)):
                if maze[current_y][current_x - i - 1] == 0:
                    maze[current_y][current_x - i - 1] = 1
    elif diff_y > 0:
        if current_y + diff_y < height:
            for i in range(diff_y):
                if maze[current_y + i + 1][current_x] == 0:
                    maze[current_y + i + 1][current_x] = 1
    elif diff_y < 0:
        if current_y + diff_y >= 0:
            for i in range(abs(diff_y)):
                if maze[current_y - i - 1][current_x] == 0:
                    maze[current_y - i - 1][current_x] = 1
    next_x = current_x + diff_x
    next_y = current_y + diff_y
    return next_x, next_y

def is_space(maze, current_x, current_y, diff_x, diff_y):
    '''check the valid space
    if the target space are located inside of the maze, it is valid.

    Args:
    :param maze (int[][]): created by init_maze()
    :param current_x (int): current location in the maze
    :param current_y (int): current location in the maze
    :param diff_x (int): difference between current_x and target_x. (target_x = current_x + diff_x)
    :param diff_y (int): difference between current_y and target_y. (target_y = current_y + diff_y)

    Returns:
    :return: boolean: return True if there are valid spaces, otherwise return False.

    >>> maze = init_maze(3, 3)
    >>> is_space(maze, 2, 1, 0, -2)
    True
    '''
    next_x = current_x + diff_x
    next_y = current_y + diff_y
    if next_x < 0 or next_x > (len(maze[0])-1) or next_y <= 0 or next_y > (len(maze)-1):
        return False
    else:
        return True

def set_direction():
    '''ready for direction at random

    Args:
    None

    Returns:
    :return: direction (int): 0 = North, 1 = East, 2 = South, 3 = West
    :return: diff_x (int): difference on x axis between current location and target location
    :return: diff_y (int): difference on y axis between current location and target location

    >>> random.seed(0)
    >>> direction, diff_x, diff_y = set_direction()
    >>> print(direction, diff_x, diff_y)
    3 -2 0
    '''
    direction = random.randint(0, 3)
    if direction == 0: # North
        return direction, 0, -2
    elif direction == 1: # East
        return direction, 2, 0
    elif direction == 2: # South
        return direction, 0, 2
    elif direction == 3: # West
        return direction, -2, 0
    else:
        print(direction, 'something wrong in set_arrow()')
        exit()

def create_maze(maze, x, y, random_seed=0):
    '''create maze from start_x & start_y by simple depth-first search

    Args:
    :param mmaze (int[][]): created by init_maze()
    :param x (int): start position in the maze
    :param y (int): start position in the maze
    :param random_seed (int): seed for random generator

    Returns:
    :return: None

    >>> maze = init_maze(3, 4)
    >>> create_maze(maze, 2, 0)
    3 -2 0
    3 -2 0
    >>> print_maze(maze)
    ----
    1100
    0000
    0000
    '''
    random.seed(random_seed)
    while(True):
        direction, diff_x, diff_y = set_direction()
        print(direction, diff_x, diff_y)
        flag = is_space(maze, x, y, diff_x, diff_y)
        if flag == True:
            x, y = dig_maze(maze, x, y, diff_x, diff_y)
            #print('new(x,y) = ', x, y)
            #print_maze(maze)
        else:
            break

if __name__ == '__main__':
    # example code to make a maze with 9 x 11
    height = 9
    width = 11
    maze1 = init_maze(height, width)
    start_x = int(width / 2)
    start_y = int(height / 2)
    maze1[start_y][start_x] = 9 # special value for start point
    print('start_x, start_y = ', start_x, start_y)
    create_maze(maze1, start_x, start_y)
    print_maze(maze1)
