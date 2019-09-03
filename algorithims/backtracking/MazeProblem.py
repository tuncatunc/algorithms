class MazeProblem:
    def __init__(self, maze):
        self.maze = maze
        self.solution = [[0 for x in range(len(maze))] for y in range(len(maze[0]))]

    def solveProblem(self):
        # Start from 0, 0
        self.solution[0][0] = 1
        if self.solve(0, 0):
          self.printSolution()
        else:
          print("❌❌❌No feasible solution is found ❌❌❌")

    def solve(self, row, col):
      if self.solutionFound(row, col):
        return True

      offsetts = [(0, 1), (0, -1), (1, 0), (-1, 0)]

      for offsett in offsetts:
        nextRow = row + offsett[0]
        nextCol = col + offsett[1]

        if self.isValid(nextRow, nextCol):
          self.solution[nextRow][nextCol] = 1

          if self.solve(nextRow, nextCol):
            return True

          # Backtrack
          self.solution[nextRow][nextCol] = 0

      return False

    # Solution is found if row and col are at the edge
    def solutionFound(self, row, col):
      return row == len(self.maze) - 1 and col == len(self.maze[0]) -1 and self.solution[row][col] == 1


    # Check row and col is in maze ranges 
    # and maze[row][col] is not obstacle (0 is obstacle)
    # and is not visited 
    def isValid(self, row, col):
      result = row >= 0 and row < len(self.maze) and col >= 0 and col < len(self.maze[0]) and self.maze[row][col] == 1 and self.solution[row][col] != 1
      return result

    def printSolution(self):
      for row in range(len(self.solution)):
        for col in range(len(self.solution[0])):
          print("S" if self.solution[row][col] is 1 else "-", end=' ')
        print()

if __name__ == "__main__":

    mazeTable = [[1, 1, 1, 1, 1],
                 [0, 0, 0, 1, 0],
                 [1, 1, 1, 1, 0],
                 [1, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1]
                 ]

    mazeProblem = MazeProblem(mazeTable)
    mazeProblem.solveProblem()
