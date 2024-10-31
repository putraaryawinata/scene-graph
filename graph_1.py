"""
1 -- 2 -- 3 -- 4
|    |    |    |
5 -- 6 -- 7 -- 8
|    |    |    |
9 -- 10-- 11-- 12

"""

import numpy as np
import networkx as nx
from matplotlib.widgets import Button

import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
nodes = range(1, 13)
G.add_nodes_from(nodes)

# Add edges
edges = [
    (1, 2), (2, 3), (3, 4),
    (1, 5), (2, 6), (3, 7), (4, 8),
    (5, 6), (6, 7), (7, 8),
    (5, 9), (6, 10), (7, 11), (8, 12),
    (9, 10), (10, 11), (11, 12)
]
G.add_edges_from(edges)

# Draw the graph
pos = {
    1: (0, 2), 2: (1, 2), 3: (2, 2), 4: (3, 2),
    5: (0, 1), 6: (1, 1), 7: (2, 1), 8: (3, 1),
    9: (0, 0), 10: (1, 0), 11: (2, 0), 12: (3, 0)
}
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
# plt.show()

import matplotlib.pyplot as plt

class GraphNavigator:
    def __init__(self, graph, pos):
        self.graph = graph
        self.pos = pos
        self.current_node = 1
        self.fig, self.ax = plt.subplots()
        self.draw_graph()
        self.create_buttons()

    def draw_graph(self):
        self.ax.clear()
        nx.draw(self.graph, self.pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', ax=self.ax)
        nx.draw_networkx_nodes(self.graph, self.pos, nodelist=[self.current_node], node_color='red', node_size=500, ax=self.ax)
        plt.draw()

    def create_buttons(self):
        axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
        axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
        self.bprev = Button(axprev, 'Previous')
        self.bnext = Button(axnext, 'Next')
        self.bprev.on_clicked(self.prev_node)
        self.bnext.on_clicked(self.next_node)

    def prev_node(self, event):
        neighbors = list(self.graph.neighbors(self.current_node))
        print(f"current_node: {self.current_node}")
        print(f"neighbors: {neighbors}")
        if neighbors:
            self.current_node = neighbors[0]
            self.draw_graph()

    def next_node(self, event):
        neighbors = list(self.graph.neighbors(self.current_node))
        if neighbors:
            self.current_node = neighbors[-1]
            self.draw_graph()

navigator = GraphNavigator(G, pos)
plt.show()