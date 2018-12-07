import networkx as nx

Graph = nx.DiGraph()
Graph.add_edges_from([(x.split()[1], x.split()[7]) for x in open('data.txt').readlines()])

# part 1
res = ''.join(nx.lexicographical_topological_sort(Graph))
print(res)

# part 2
res = max(sum(map(lambda x: ord(x.lower()) - 96 + 60, path))
          for path in nx.all_simple_paths(Graph, source=res[0], target=res[-1]))

print(res)
