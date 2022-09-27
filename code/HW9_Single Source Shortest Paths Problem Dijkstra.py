from collections import defaultdict
import heapq
def dij(edges, source, sink):
    G = defaultdict(list)
    for l, r, c in edges:
        G[l].append((c,r))
    q, v = [(0, source, [])], set()
    heapq.heapify(q)
    while q:
        (cost, node, edge) = heapq.heappop(q)
        if node not in v:
            v.add(node)
            edge = edge + [node]
            if node == sink:
                return (cost)
            for c, neighbour in G[node]:
                if neighbour not in v:
                    heapq.heappush(q, (cost+c, neighbour, edge))
    return float("inf")

while True:
    try:
      _in = input()
      edges = []
      row = _in.split(",")
      for i in range(0,len(row)-2, 3):
        temp = []
        temp.append(row[i])
        temp.append(row[i+1])
        temp.append(int(row[i+2]))
        edges.append(temp)
      print ("The shortest distance from "+ row[-2] + " to " + row[-1] + " is " + str(dij(edges, row[-2], row[-1])))
    except:
      break