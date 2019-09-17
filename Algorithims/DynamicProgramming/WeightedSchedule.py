# Given list of intervals (start, end, value)
# Find the subset of interwals where total weights selected items maximize total value
# Constraint is intervals must not collapse on each other
from collections import namedtuple
Interval = namedtuple('Interval', 'start end weight')

class WeightedScheduleProblem:
  # Intervals = []
  def __init__(self, intervals):
    self.intervals = intervals
    self.solution = []
    self.N = len(intervals)

  def findLastNonIntersectingInterval(self, n):
    for i in reversed(range(n)):
      if self.intervals[i].end <= self.intervals[n].start:
        return i

    # Not found
    return None

  def solve(self, n):
    if n == 0:
      return self.intervals[0].weight

    lastNonIntersectingInterval = self.findLastNonIntersectingInterval(n)
    included = 0
    excluded = 0

    if lastNonIntersectingInterval != None:
      included = self.solve(lastNonIntersectingInterval) + self.intervals[n].weight

    excluded = self.solve(n - 1)

    return max(included, excluded)

  def sortIntervalsByFinishTime(self):
    self.intervals = sorted(self.intervals, key= lambda i: i.end)

  def solveProblem(self):
    self.sortIntervalsByFinishTime()

    maxWeight = self.solve(self.N -1)
    print(f"Max weight {maxWeight}")

intervals = [Interval(1, 2, 50), Interval(3, 5, 20), Interval(6, 19, 100), Interval(2, 100, 200)]
weightedScheduleProblem = WeightedScheduleProblem(intervals)
weightedScheduleProblem.solveProblem()


