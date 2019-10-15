class DisjointSet:
  def __init__(self, N):
    self.parent = [-1 for N in range(N)]
    self.N = N

  def makeSet(self, v):
    self.parent[v] = v

  def unionSets(self, u, v):
    uf = self.findSet(u)
    vf = self.findSet(v)

    if uf != vf:
      self.parent[uf] = vf

  def findSet(self, u):
    if self.parent[u] == u:
      return u

    return self.findSet(self.parent[u])
