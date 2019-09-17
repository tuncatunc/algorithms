# Given W, V, C
# Find items that maximize total values of knapsack capacity C


class KnapsackProblem:
  # W: Weights
  # V: Values
  # C: Capacity
  # N: Number of items
  def __init__(self, W, V, C, N):
    self.W = W
    self.V = V
    self.C = C
    self.N = N
    self.max = 0

    self.solution = set([])

    # Memo for the memoization solution
    self.memo = [[None for n in range(C + 1)] for w in range(N)]

  # n: Item index
  # C: Remaining capacity
  def solve(self, n, c):
    # Base case
    if n < 0 or c <= 0:
      return 0

    if self.W[n] > c:
      return self.solve(n-1, c)

    # Nth item is included
    included = self.solve(n-1, c - self.W[n]) + self.V[n]

    # Nth item is not included
    notIncluded = self.solve(n-1, c)

    if included > notIncluded:
      self.solution.add(n)

    result = max(included, notIncluded)
    return result

  # n: Item index
  # C: Remaining capacity
  def solveMemo(self, n, c):

    # Base case
    if n < 0 or c <= 0:
      return 0
    
    if self.W[n] > c:
      return 0

    # Return memoized solution if any
    if self.memo[n][c] != None:
      return self.memo[n][c]

    included = self.solveMemo(n-1, c - self.W[n]) + self.V[n]
    notIncluded = self.solveMemo(n - 1, c)

    if included > notIncluded:
      self.solution.add(n)

    result = max(included, notIncluded)
    self.memo[n][c] = result

    return result

  def printSolution(self):
    print("=============================")
    print(f"Max knapsack value {self.max}")
    print(f"Items {self.solution}")
    print(f"Weights {self.W}")
    print(f"Values {self.V}")


  # Memoized solution
  def solveProblemMemoized(self):
    self.max = self.solveMemo(numOfItems - 1, capacityOfKnapsack)

  # Recursive solution
  def solveProblem(self):
    self.max = self.solve(numOfItems - 1, capacityOfKnapsack)
    

numOfItems = 5
capacityOfKnapsack = 10
values = [5, 3, 5, 3, 2]
weights = [1, 2, 4, 2, 5]

knapsack = KnapsackProblem(
    weights, values, capacityOfKnapsack, numOfItems)
knapsack.solveProblem()
knapsack.printSolution()

knapsack.solveProblemMemoized()
knapsack.printSolution()
