class Node(object):

  def __init__(self,name):
    self.name = name

  def getName(self):
    return self.name

  def __str__(self):
    return self.name

class Edge(object):

  def __init__(self, src, dest):
    self.src = src
    self.dest = dest

  def getSource(self):
    return self.src

  def getDest(self):
    return self.dest

  def __str__(self):
    return self.src.getName() + '->' + self.dest.getName()    

class Digraph(object):

  def __init__(self):
    self.nodes = []
    self.edges = {}

  def addNode(self, node):
    if node in self.nodes:
      raise ValueError("Duplicate node")
    else:
      self.nodes.append(node)
      self.edges[node] = []

  def addEdge(self, edge):
    src = edge.getSource()
    dest = edge.getDest()
    if not (src in self.nodes and dest in self.nodes):
      raise ValueError("Node not in graph")
    self.edges[src].append(dest)

  def childrenOf(self, node):
    return self.edges[node]

  def hasNode(self, node):
    return node in self.nodes

  def __str__(self):
    ret = ''
    for src in self.nodes:
      for dest in self.edges[src]:
        ret = ret + src.getName() + '->' + dest.getName() + '\n'
    return ret[:-1]

def createGraph(kind = "BFS"):
  nodes = []
  for name in range(6):
    nodes.append(Node(str(name)))
  g = Digraph()
  for n in nodes:
    g.addNode(n)
  g.addEdge(Edge(nodes[0], nodes[1]))
  g.addEdge(Edge(nodes[1], nodes[2]))
  g.addEdge(Edge(nodes[2], nodes[3]))
  g.addEdge(Edge(nodes[3], nodes[4]))
  g.addEdge(Edge(nodes[3], nodes[5]))
  g.addEdge(Edge(nodes[0], nodes[2]))
  g.addEdge(Edge(nodes[1], nodes[0]))
  g.addEdge(Edge(nodes[3], nodes[1]))
  g.addEdge(Edge(nodes[4], nodes[0]))
  if kind == "BFS":
    sp = BFS(g, nodes[0], nodes[5], True)
  else:
    sp = DFS(g, nodes[0], nodes[5], [], None, True)
  return sp

def printPath(path):
  result = ''
  for i in range(len(path)):
    result = result + str(path[i])
    if i != len(path) - 1:
      result = result + '->'
  return result

def BFS(g, start, end, toPrint = False):
  initPath = [start]
  pathQueue = [initPath]
  if toPrint:
    print("Current BFS path :", printPath(initPath))
  while len(pathQueue) != 0:
    tmpPath = pathQueue.pop(0)
    print('Current BFS path :', printPath(tmpPath))
    lastNode = tmpPath[-1]
    if lastNode == end:
      return tmpPath
    for nextNode in g.childrenOf(lastNode):
      if nextNode not in tmpPath:
        newPath = tmpPath + [nextNode]
        pathQueue.append(newPath)
  return None

def DFS(g, start, end, path, shortest, toPrint = False):
  path = path + [start]
  if toPrint:
    print("Current DFS path :", printPath(path))
  if start == end:
    return path
  for node in g.childrenOf(start):
    if node not in path:
      if shortest == None or len(path) < len(shortest):
        newPath = DFS(g, node, end, path, shortest, toPrint)
        if newPath != None:
          shortest = newPath
  return shortest

if __name__ == "__main__":
  b = createGraph()
  print("Shortest path found by BFS ", printPath(b)) 
  d = createGraph("DFS")
  print("Shortest path found by DFS ", printPath(d)) 
