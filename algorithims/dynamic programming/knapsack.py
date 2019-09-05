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

  def printSolution(self):
    print(f"Max knapsack value {self.max}")
    print(f"Items {self.solution}")

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