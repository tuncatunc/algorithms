class ColoringProblem:
    def __init__(self, adj, N, C):
        self.adj = adj  # Adjecency matrix
        self.N = N  # nodes
        self.C = C  # colors

        # Colors assigned to each node
        self.colors = [None for x in range(N)]

    def solveProblem(self):
        # First node is colored 0
        self.colors[0] = 0

        if self.solve(1):
            self.printSolution()
        else:
            print("No feasible solution is found 💥")

    def printSolution(self):
      colorMap = {
        0: "❤",
        1: "🧡",
        2: "💛",
        3: "💚",
        4: "💙",
      }

      for idx, c in enumerate(self.colors):
        print(f"Node: {idx} Color: {colorMap[c]}")

    # Node index is valid
    def isValid(self, nodeIndex):
        return nodeIndex > 0 and nodeIndex < self.N

    # Feasible to color node index with color ?

    def isFeasible(self, nodeIndex, colorIndex):
        # Return False if any adjacent node has the same color
        for adjNodeIndex in range(self.N):
            # Same Color
            if self.isConnected(nodeIndex, adjNodeIndex) and self.colors[adjNodeIndex] == colorIndex:
                return False

        return True

    def isConnected(self, first, second):
        return adj[first][second] is 1

    def solve(self, nodeIndex):

        # Base case
        # All nodes are colored
        if (nodeIndex == self.N):
            return True

        for colorIndex in range(self.C):
            if self.isFeasible(nodeIndex, colorIndex):
                self.colors[nodeIndex] = colorIndex

                # Solve subproblem
                if self.solve(nodeIndex + 1):
                    return True

            # Backtrack
            self.colors[nodeIndex] = None


if __name__ == "__main__":
    # Adjacency matrix
    adj = [[0, 1, 1, 1, 0],
           [1, 0, 1, 0, 1],
           [1, 1, 0, 1, 0],
           [1, 1, 1, 0, 1],
           [0, 0, 0, 1, 0]
           ]

    # Try to solve with 3 colors
    coloringProblem = ColoringProblem(adj, 5, 3)
    coloringProblem.solveProblem()

    # Try to solve with 4 colors
    coloringProblem = ColoringProblem(adj, 5, 4)
    coloringProblem.solveProblem()
