def isValid(maze, point):
    COL = len(maze[0])
    ROW = len(maze)
    x = point[0]
    y = point[1]

    return x >= 0 and x < COL and y >= 0 and y < ROW and maze[x][y] != 9

# Target point is 2
def isTarget(maze, point):
    return maze[point[0]][point[1]] == 2

def backTrace(parents, node):
  path = []
  x = node[0]
  y = node[1]
  parent = parents[x][y]
  while parent:
    path.append(parent)
    x = parent[0]
    y = parent[1]
    parent = parents[x][y]
  return path

def searchMaze(maze, start):
    visited = []
    queue = []

    neighs = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    # 2D array of parent node of each cell in the maze
    parents = [[None for x in range(len(maze[0]))] for y in range(len(maze))]

    # start, distance, previous node
    queue.append((start, 0, None))

    while queue:
        q = queue.pop(0)
        node = q[0]
        distance = q[1]
        if isTarget(maze, node):
            path = backTrace(parents, node)
            return (path, distance)
        visited.append(node)
        for neigh in neighs:
            neighPoint = (node[0] + neigh[0], node[1] + neigh[1])
            if isValid(maze, neighPoint) and neighPoint not in visited:
                parents[neighPoint[0]][neighPoint[1]] = node
                queue.append((neighPoint, distance + 1, node))

