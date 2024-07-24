import networkx as nx

import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(n=100, p=0.05)

plt.figure(figsize=(12, 12))
nx.draw(G, node_size=50, with_labels=False)

plt.savefig('output.png')