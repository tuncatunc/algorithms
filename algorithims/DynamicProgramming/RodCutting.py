class RodCutting:
  def __init__(self, values, lengths, rodLength):
    self.values = values
    self.lengths = lengths
    self.rodLength = rodLength
    self.N = len(values)
    self.dpTable = [None for i in range(rodLength + 1)]

  def solve(self, len):
    # Base case
    # Leaf of the node has been reached

    if len <= 0:
      return 0

    localMaxValue = 0

    # For each cut rod length
    for i in range(self.N):
      if len >= self.lengths[i]:
        result = self.solve(len - self.lengths[i]) + self.values[i]

      if result  > localMaxValue:
        localMaxValue = result

    return localMaxValue

  def solveDynamic(self, len):
    # Base case
    # Leaf of the node has been reached

    # If there is saved solution to subproblem
    if self.dpTable[len] != None:
      return self.dpTable[len]

    if len <= 0:
      return 0

    localMaxValue = 0

    # For each cut rod length
    for i in range(self.N):
      if len >= self.lengths[i]:
        result = self.solve(len - self.lengths[i]) + self.values[i]

      if result  > localMaxValue:
        localMaxValue = result

    self.dpTable[len] = localMaxValue
    return localMaxValue

rodLength = 5
values = [2, 5, 7, 3]
lengths = [1, 2, 3, 4]
rodCutting = RodCutting(values, lengths, 5)
result = rodCutting.solve(rodLength)
print(f"Recursive solution Max:{result}")

result = rodCutting.solveDynamic(rodLength)
print(f"Dynamic solution Max:{result}")
