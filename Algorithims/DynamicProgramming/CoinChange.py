# Given ser of coins
# How many ways  the coins can be combined in order to get the total M
class CoinChange:
  def __init__(self, M, coins):
    self.M = M
    self.coins = coins
    self.resultSet = []


  def isFound(self, subset):
    for ss in self.resultSet:
      sorted1 = sorted(ss)
      sorted2 = sorted(subset)

      result = True
      if len(sorted1) == len(sorted2):
        for i in range(len(sorted1)):
          if sorted1[i] != sorted2[i]:
            result = False
      else:
        result = False

      if result == True:
        return True

    return False
  
  def solve(self, amount, subset):

    # Base case
    # Only leaf nodes are count
    if amount == 0:
      # Check if this subset of numbers are already added
      if not self.isFound(subset):
        self.resultSet.append(subset)
        return 1
      else:
        return 0

    # Base case
    result = 0
    for coin in self.coins:
      # Dont branch to solve(-1), 
      # Solving problems for negative amounts is meaningless
      if amount >= coin: 
        result += self.solve(amount - coin, subset + [coin])

    return result

coins = [1, 2, 3]
amount = 4
coinChangeProblem = CoinChange(amount, coins)
result = coinChangeProblem.solve(amount, [])
print(coinChangeProblem.resultSet)

