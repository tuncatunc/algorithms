class NQueens:
  def __init__(self, N):
    self.N = N
    self.board = [[None for x in range(N)] for y in range(N)]
  
  def isValid(self, row, col):
    return row < self.N and col < self.N

  # Is placing a new queen at row, col attacks other queens
  # Check if there any queens on the same row or col or diagonal line
  def isAttacking(self, row, col):
    # Check row
    for c in range(self.N):
      if c != col and self.board[row][c] != None:
        return True

    # Check column
    for r in range(self.N):
      if r != row and self.board[r][col] != None:
        return True

    # Check diagonal
    for d in range(1, self.N-1):
      # Check diagonals
      nextRow = row + d
      prevRow = row - d
      nextCol = col + d
      prevCol = col - d
      if (self.isValid(nextRow, nextCol) and self.board[nextRow][nextCol] != None or
          self.isValid(nextRow, prevCol) and self.board[nextRow][prevCol] != None or
          self.isValid(prevRow, nextCol) and self.board[prevRow][nextCol] != None or
          self.isValid(prevRow, prevCol) and self.board[prevRow][prevCol] != None
        ):
        return True
    
    return False

  def solve(self, col):
    # Base case
    if col == self.N:
      return True

    for row in range(self.N):

      if not self.isAttacking(row, col):
        self.board[row][col] = True
        if self.solve(col + 1):
          return True
      
      # Backtrack
      self.board[row][col] = None

    return False          

  def printBoard(self):
    for row in range(self.N):
      for col in range(self.N):
        print ('👑' if self.board[row][col] else '🔲', end=' ')
      print()


nQueensProblem = NQueens(8)
if nQueensProblem.solve(0):
  nQueensProblem.printBoard()
else:
  print("💥No feasible solution")
