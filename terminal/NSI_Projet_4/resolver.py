import myc


def find_start_end_N(grid,app=True):
    entry = set()
    start_pos = None
    end_pos = None

    # Check first and last rows
    for j in range(len(grid[0])):
        if grid[0][j] == 0:
            entry.add((0, j))
        if grid[-1][j] == 0:
            entry.add((len(grid) - 1, j))

    # Check first and last columns
    for i in range(len(grid)):
        if grid[i][0] == 0:
            entry.add((i, 0))
        if grid[i][-1] == 0:
            entry.add((i, len(grid[0]) - 1))

    # Find start and end positions
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element == 2:
                if start_pos and app:
                    raise ValueError("Multiple start positions")
                start_pos = (i, j)
            elif element == 3:
                if end_pos and app:
                    raise ValueError("Multiple end positions")
                end_pos = (i, j)
    
    if start_pos is not None and end_pos is not None:
        return start_pos, end_pos
    if len(entry) < 1 and app:
        raise RuntimeError("not enough entries")
    if start_pos is not None and end_pos is None:
        if not app and len(entry) < 1:
            return start_pos , None
        end_pos = entry.pop()
        grid[end_pos[0]][end_pos[1]] = 3
        return start_pos, end_pos
    elif start_pos is None and end_pos is not None:
        if not app and len(entry) < 1:
            return None , end_pos
        start_pos = entry.pop()
        grid[start_pos[0]][start_pos[1]] = 2
        return start_pos, end_pos
    if len(entry) < 2 and app:
        raise RuntimeError("not enough entries")
    if start_pos is None and end_pos is None:
        if not app and len(entry) < 1:
            return None , None
        start_pos = entry.pop()
        grid[start_pos[0]][start_pos[1]] = 2
        if not app and len(entry) < 1:
            return start_pos , None
        end_pos = entry.pop()
        grid[end_pos[0]][end_pos[1]] = 3
        return start_pos, end_pos

    raise RuntimeError("unreachable")


###! def find_start_end_W(grid):
###!     # TODO
###!     entry = []
###!     size = myc.project.get_size()
###! 
###!     # Check first and last rows
###!     for j in range(size[1]+1):
###!         if len(grid[f"({0},{j})"]):
###!             entry.append((0, j))
###!         if len(grid[f"({size[0]},{j})"]):
###!             entry.append((size[0], j))
###! 
###!     # Check first and last columns
###!     for i in range(size[0]+1):
###!         if len(grid[f"({i},{0})"]):
###!             entry.append((i, 0))
###!         if len(grid[f"({i},{size[0]})"]):
###!             entry.append((i, size[0]))


def neighbors_N(x, y, grid):
    rows, cols = myc.project.get_size(grid)
    n = []
    if x-1 >= 0 and (grid[x-1][y] != 1 or grid[x-1][y] != True):
        n.append((x-1, y))
    if x+1 <= rows-1 and (grid[x+1][y] != 1 or grid[x+1][y] != True):
        n.append((x+1, y))
    if y-1 >= 0 and (grid[x][y-1] != 1 or grid[x][y-1] != True):
        n.append((x, y-1))
    if y+1 <= cols-1 and (grid[x][y+1] != 1 or grid[x][y+1] != True):
        n.append((x, y+1))
    return n


###! def neighbors_W(x, y, grid):
###!     return grid[[f"({x},{y})"]]

# BFS


def BFS(start=None, end=None, T=None, G=None):
    if G is None:
        G = myc.project().conv_to_N().DATA

    def BFS_N(start, end, T, G):
        file = [start]
        visited = set([start])
        # print("start",start,"end",end,"T",T,"G",G,"queue",queue,"visited",visited)
        i = 0
        while file and (i < T if T is not None else True):
            # print(queue,visited)
            node = file.pop(0)
            i += 1
            if node == end:
                return (None,list(visited))
            # print(node,"neighbors_N",neighbors_N(*node,G))
            for neighbor in neighbors_N(*node,G):
                if neighbor not in visited:
                    visited.add(neighbor)
                    file.append(neighbor)

        return (list(visited), None)

    ###! def BFS_W(start=None, end=None, T=None, G=None):
    ###!     # TODO
    ###!     queue = [(start, [start])]
    ###!     visited = set([start])
    ###! 
    ###!     while queue and (len(visited) < T if T is not None else True):
    ###!         (node, path) = queue.pop(0)
    ###!         if node == end:
    ###!             return (None, path)
    ###!         for neighbor in neighbors_N(G, node):
    ###!             if neighbor not in visited:
    ###!                 # TODO
    ###!                 # NO
    ###!                 pass
    ###!                 # visited.add(neighbor)
    ###!                 # queue.append((neighbor, path + [neighbor]))

    if isinstance(G, dict):
        myc.project().conv_to_N()
        return BFS(start=start,end=end,T=T,G=G)
        ###! if start is None or end is None:
        ###!     start, end = find_start_end_W(G)
        ###! return BFS_W(start=start, end=end, T=T, G=G)
    elif isinstance(G, list):
        if start is None or end is None:
            start, end = find_start_end_N(G)
        return BFS_N(start=start, end=end, T=T, G=G)
    raise RuntimeError("idk man")


# DFS
def DFS(start=None, end=None, T=None, G=None):
    if G is None:
        G = myc.project().conv_to_N().DATA

    def DFS_N(start, end, T, G):
        pile = [start]
        visited = set([start])
        # print("start",start,"end",end,"T",T,"G",G,"queue",queue,"visited",visited)
        i = 0
        while pile and (i < T if T is not None else True):
            # print(queue,visited)
            node = pile.pop()
            i += 1
            if node == end:
                return (None,list(visited))
            # print(node,"neighbors_N",neighbors_N(*node,G))
            for neighbor in neighbors_N(*node,G):
                if neighbor not in visited:
                    visited.add(neighbor)
                    pile.append(neighbor)

        return (list(visited), None)

    ###! def DFS_W(start=None, end=None, T=None, G=None):
    ###!     # TODO
    ###!     if start is None or end is None:
    ###!         start, end = find_start_end_W(G)
    ###! 
    ###!     queue = [(start, [start])]
    ###!     visited = set([start])
    ###! 
    ###!     while queue and (len(visited) < T if T is not None else True):
    ###!         (node, path) = queue.pop(0)
    ###!         if node == end:
    ###!             return (None, path)
    ###!         for neighbor in neighbors_N(G, node):
    ###!             if neighbor not in visited:
    ###!                 # TODO
    ###!                 # NO
    ###!                 pass
    ###!                 # visited.add(neighbor)
    ###!                 # queue.append((neighbor, path + [neighbor]))

    if isinstance(G, dict):
        myc.project().conv_to_N()
        return DFS(start=start,end=end,T=T,G=G)
        ###! if start is None or end is None:
        ###!     start, end = find_start_end_W(G)
        ###! return BFS_W(start=start, end=end, T=T, G=G)
    elif isinstance(G, list):
        if start is None or end is None:
            start, end = find_start_end_N(G)
        return DFS_N(start=start, end=end, T=T, G=G)
    raise RuntimeError("idk man")


# Dijkstra
def Dijkstra(start=None, end=None, T=None, G=None):
    raise NotImplementedError


if __name__ == "__main__":
    # utilise l'exemple de l'énoncer
    pass
    ###! G = dict()
    ###! G['a'] = ['b', 'c']
    ###! G['b'] = ['a', 'd', 'e']
    ###! G['c'] = ['a', 'd']
    ###! G['d'] = ['b', 'c', 'e']
    ###! G['e'] = ['b', 'd', 'f', 'g']
    ###! G['f'] = ['e', 'g']
    ###! G['g'] = ['e', 'f', 'h']
    ###! G['h'] = ['g']
    ###! assert BFS(start='b', G=G) == ['b', 'a', 'd', 'e', 'c', 'f', 'g', 'h']
