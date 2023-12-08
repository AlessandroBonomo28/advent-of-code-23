# importing networkx 
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt


def plot_default(network):
    g = nx.Graph()
    for node in network:
        g.add_edge(node[0], node[1][0])
        g.add_edge(node[0], node[1][1])
    nx.draw(g, with_labels=True)
    plt.show()

def plot_nicely(network):
    g = nx.Graph()
    for node in network:
        g.add_edge(node[0], node[1][0])
        g.add_edge(node[0], node[1][1])
    #pos = nx.spring_layout(g, k=0.15, iterations=100)
    pos = nx.spring_layout(g, scale=2)
    nx.draw(g, pos, with_labels=True)
    plt.show()

if __name__ == "__main__":
    # Create a graph
    g = nx.Graph()

    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_node(9)

    nx.draw(g, with_labels=True)
    plt.savefig("graph.png")