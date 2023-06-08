import random
import myc
import resolver

def choose_start_end(row_size, col_size):
    # choose start wall
    if random.randint(0, 1) == 1:
        # 1/2 n or s
        # ###
        #
        # ###
        if random.randint(0, 1) == 1:
            # 1/4 n
            # ####
            #
            #
            start = (0,random.randint(0, col_size-1))
            orint = "n"
        else:
            # 1/4 s
            #
            #
            # ####
            start = (row_size-1,random.randint(0, col_size-1))
            orint = "s"
    else:
        # 1/2 e or w
        # ##   ##
        # ##   ##
        # ##   ##
        if random.randint(0, 1) == 1:
            # 1/4 w
            start = (random.randint(0, row_size-1),0)
            orint = "w"
        else:
            # 1/4 e
            start = (random.randint(0, row_size-1),col_size-1)
            orint = "e"

    # my logic is undeniable
    # well as a matter of fact it look to weird
    # 1/3 opposite side
    if orint == "n":
        # s
        end = (row_size-1,random.randint(0, col_size-1))
    elif orint == "s":
        # n
        end = (0,random.randint(0, col_size-1))
    elif orint == "e":
        # w
        end = (random.randint(0, row_size-1),0)
    elif orint == "w":
        # e
        end = (random.randint(0, row_size-1),col_size-1)
    
    return start , end

def generator():
    MIN_SIZE = 5
    MAX_SIZE = 10

    maze = []
    row_size = random.randint(MIN_SIZE, MAX_SIZE)
    col_size = random.randint(MIN_SIZE, MAX_SIZE)

    for _ in range(row_size):
        maze.append([0] * col_size)

    start , end = choose_start_end(row_size, col_size)

    ##########################################################################
    # DFS modified
    stack = [start]
    visited = set([start])

    while stack:
        x, y = stack.pop()
        maze[x][y] = 0
        if (x,y) == end:
            break

        neighbors = resolver.neighbors_N(x, y, maze)
        unvisited_neighbors = [n for n in neighbors if n not in visited]
    
        # If there are unvisited neighbors, choose one randomly and add it to the stack
        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            visited.add(next_cell)
            stack.append(next_cell)
        
    for i,row in enumerate(maze):
        for j,case in enumerate(row):
            if (i,j) not in visited:
                maze[i][j] = 1
    
    maze[start[0]][start[1]] = 2
    maze[end[0]][end[1]] = 3

    myc.project().DATA = maze
    myc.project().DATA_W = False
