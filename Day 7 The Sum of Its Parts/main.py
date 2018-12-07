import networkx as nx

Graph = nx.DiGraph()
Graph.add_edges_from([(x.split()[1], x.split()[7]) for x in open('data.txt').readlines()])
print(''.join(nx.lexicographical_topological_sort(Graph)))
