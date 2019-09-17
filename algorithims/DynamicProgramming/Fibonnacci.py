class FibonacciProblem:
  def __init__(self, N):
    self.N = N
    self.memo = [None for x in range(N + 1)]
    self.memo[0] = 0
    self.memo[1] = 1

  def solve(self, N):

    if self.memo[N] != None:
      return self.memo[N]

    self.memo[N-1] = self.solve(N-1)
    self.memo[N-2] = self.solve(N-2)
    self.memo[N] = self.memo[N - 1] + self.memo[N - 2]
    return self.memo[N]

N = 100
fib = FibonacciProblem(N)
print(f"Fibonacci ({N})-> {fib.solve(N)}")
print("💌")
