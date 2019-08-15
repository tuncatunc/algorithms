class Knapsack:
  def __init__(self, count, weights, values, capacity):
    self.count = count
    self.weights = weights
    self.values = values
    self.capacity = capacity
    self.solution = set([])
    self.memorizationTable = [[None for x in range(capacity + 1)] for y in range(count)]

  def RecursiveSolution(self, n, C):
    # Base case
    # No items is left or no capacity is left
    if n == 0 or C <= 0:
      return 0

    # Don't include item if it exceeds capacity
    if self.weights[n] > C:
      return self.RecursiveSolution(n-1, C)

    tmp1 = self.RecursiveSolution(n-1, C) # Nth item is not included
    tmp2 = self.values[n] + self.RecursiveSolution(n-1, C - self.weights[n]) # Nth item is included

    if (tmp2 > tmp1):
      self.solution.add(self.values[n])

    return max(tmp1, tmp2)

  # Remember some intermediate results
  # https://www.youtube.com/watch?v=xOlhR_2QCXY
  def Memorization(self, n, C):
    if self.memorizationTable[n][C] != None:
      return self.memorizationTable[n][C]

    result = 0

    # Base checks
    if n == 0 or C <= 0:
      result = 0

    # If item's weight exceeds capacity don't include it at all
    elif self.weights[n] >= C:
      result = 0
    
    else:
      included = self.Memorization(n-1, C - self.weights[n]) + self.values[n]
      notIncluded = self.Memorization(n-1, C)
      result = max(included, notIncluded)
      
      if (included > notIncluded):
        self.solution.add(self.values[n])

    
    self.memorizationTable[n][C] = result
    return result

  def SolveWithRecursiveSolution(self):
    # Empty solution set
    self.solution = set([])
    return self.RecursiveSolution(4, self.capacity)

  def UsingDynamicProgramming(self):
    self.solution = set([])
    return self.Memorization(len(self.values) - 1, 10)

values = [5, 3, 5, 3, 2]
weights = [1, 2, 4, 2, 5]

knapsack = Knapsack(len(values), weights, values, 10)
knapsack.SolveWithRecursiveSolution()
print("Recursive Solution:", knapsack.solution)

knapsack.UsingDynamicProgramming()
print("Memoization Dynamic Solution:", knapsack.solution)
