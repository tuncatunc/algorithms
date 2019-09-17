class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.random = None

  def _copy_(self):
    return type(self)(self.value)

class LinkedList:
  def __init__(self, start):
    self.start = start

  def clone(self):
    orgToClone = {}
    node = self.start

    while node != None:
      clone = Node(node.value)
      orgToClone[hash(node)] = clone
      node = node.next

    node = self.start
    while node != None:
      if node.next != None:
        orgToClone[hash(node)].next = orgToClone[hash(node.next)]

      if node.random != None:
        orgToClone[hash(node)].random = orgToClone[hash(node.random)]

      node = node.next

    return orgToClone[hash(self.start)]

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

n1.random = n3
n2.random = n5
n3.random = n1
n4.random = n4
n5.random = n1

list1 = LinkedList(n1)
clist1 = list1.clone()
print(clist1)
