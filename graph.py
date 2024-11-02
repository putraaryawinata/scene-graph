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
        axup = plt.axes([0.48, 0.05, 0.1, 0.075])
        axdown = plt.axes([0.59, 0.05, 0.1, 0.075])
        axleft = plt.axes([0.7, 0.05, 0.1, 0.075])
        axright = plt.axes([0.81, 0.05, 0.1, 0.075])
        self.bup = Button(axup, 'Up')
        self.bdown = Button(axdown, 'Down')
        self.bleft = Button(axleft, 'Left')
        self.bright = Button(axright, 'Right')
        self.bup.on_clicked(self.up_node)
        self.bdown.on_clicked(self.down_node)
        self.bleft.on_clicked(self.left_node)
        self.bright.on_clicked(self.right_node)

    def up_node(self, event):
        neighbors = list(self.graph.neighbors(self.current_node))
        if any(neighbor < self.current_node for neighbor in neighbors):
            self.current_node = neighbors[0]
            self.draw_graph()
        else:
            print("No up node")
            pass
    
    def left_node(self, event):
        neighbors = list(self.graph.neighbors(self.current_node))
        neighbors = [neighbor for neighbor in neighbors if neighbor < self.current_node]
        if neighbors:
            self.current_node = neighbors[-1]
            self.draw_graph()
        else:
            print("No left node")
            pass

    def right_node(self, event):
        neighbors = list(self.graph.neighbors(self.current_node))
        neighbors = [neighbor for neighbor in neighbors if neighbor > self.current_node]
        if neighbors:
            self.current_node = neighbors[0]
            self.draw_graph()
        else:
            print("No right node")
            pass
    
    def down_node(self, event):
        neighbors = list(self.graph.neighbors(self.current_node))
        if any(neighbor > self.current_node for neighbor in neighbors):
            self.current_node = neighbors[-1]
            self.draw_graph()
        else:
            print("No down node")
            pass

if __name__ == "__main__":

    # Create a graph
    G = nx.Graph()

    # Add nodes
    nodes = range(1, 13)
    G.add_nodes_from(nodes)

    # Add edges
    edges = [
        (1, 2), (2, 3), (3, 4), (7, 2),
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

    navigator = GraphNavigator(G, pos)
    plt.show()