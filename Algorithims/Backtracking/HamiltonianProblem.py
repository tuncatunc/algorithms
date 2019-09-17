class HamiltonianProblem:
  def __init__(self, adj, N):
    self.adj = adj
    self.N = N
    self.path = []

  def printSolution(self):
    [print(i, end='💫') for i in self.path]

  def isValid(self, nodeIndex):
    return nodeIndex > 0 and nodeIndex < self.N

  def isAdjacent(self, firstNodeIndex, secondNodeIndex):
    return self.adj[firstNodeIndex][secondNodeIndex] == 1

  def isVisited(self, nodeIndex):
    return nodeIndex in self.path

  def solveHamiltonianPath(self):
    self.path.append(0)
    return self.solve(1)

  def solve(self, nodeIndex):
    # last node is adjacent to starting node 0
    if nodeIndex == self.N:
      if self.isAdjacent(nodeIndex - 1, 0):
        return True
      else:
        return False

    # For all adjacent and not visited nodes
    for nextNodeIndex in range(self.N):
      print(f"index: {nodeIndex} next: {nextNodeIndex}")
      if (self.isValid(nextNodeIndex) and 
          self.isAdjacent(nextNodeIndex, nodeIndex) and 
          not self.isVisited(nextNodeIndex)):
        self.path.append(nextNodeIndex)

        # Solve the subproblem
        if (self.solve(nodeIndex + 1)):
          return True

        # Cannot find a solution for the nodeIndex + 1
        # Backtrack by removing last item in the path
        self.path.pop()

      

adj = [
  [0, 1, 0],
  [1, 0, 1],
  [1, 1, 0]
]
    
problem = HamiltonianProblem(adj, len(adj))
if problem.solveHamiltonianPath():
  problem.printSolution()
else:
  print("No hamiltonian path is found 💥")