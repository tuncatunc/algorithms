from collections import namedtuple

Point = namedtuple('Point', 'row col')
Q = namedtuple('Q', 'point distance')

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])

    def isEdge(self, point):
        return (point.row == 0 or point.row == self.ROWS - 1 or
                point.col == 0 or point.col == self.COLS - 1)

    def isValid(self, point):
        return (point.row >= 0 and
                point.row < self.ROWS and
                point.col >= 0 and
                point.col < self.COLS and
                self.matrix[point.row][point.col] != 1)

    def BFS_nearest_boundry(self, start):
        visited = [start]
        queue = [Q(start, 0)]
        minDistance = Q(Point(-1, -1), 999999)

        neighs = [
            Point(0, -1),  # LEFT
            Point(-1, 0),  # TOP
            Point(0, 1),  # RIGHT
            Point(1, 0)  # BOTTOM
        ]

        while queue:
            q = queue.pop(0)
            # q Point
            qP = q.point
            qD = q.distance

            # print("BFS=>", q)
            if self.isEdge(q.point):
                # print("Edge is reached", q)
                if q.distance < minDistance.distance:
                  minDistance = q

            for neigh in neighs:
                # Neigh point
                nextPoint = Point(qP.row + neigh.row, qP.col + neigh.col)
                if self.isValid(nextPoint) and nextPoint not in visited:
                    visited.append(nextPoint)
                    queue.append(Q(nextPoint, qD + 1))
        print("Min distance to edge", minDistance)

matrix = [
    [1, 1, 1, 0, 1],
    [1, 0, 2, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

graph = Graph(matrix)
graph.BFS_nearest_boundry(Point(1, 2))
