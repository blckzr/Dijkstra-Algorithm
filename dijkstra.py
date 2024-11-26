import matplotlib.pyplot as plt
import networkx as nx
from graph import Graph

# Graph setup
def initGraph():
    g = Graph(7)
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for i, v in enumerate(vertices):
        g.add_vertex_data(i, v)

    # (Start, End, Weight)
    edges = [
        (5, 0, 4), (5, 2, 3), (0, 2, 2), (0, 3, 4), (0, 4, 3), 
        (2, 3, 2), (3, 4, 4), (3, 1, 3), (1, 6, 2)
    ]

    for start, end, weight in edges:
        g.add_edge(start, end, weight)

    return g

def initVisual(g, start_vertex):
    distances, previous = g.dijkstra(start_vertex)

    # Visualizing the graph
    G = nx.DiGraph()

    # Add nodes and edges
    for i in range(g.size):
        G.add_node(g.vertex_data[i])
    for u in range(g.size):
        for v in range(g.size):
            if g.adj_matrix[u][v] != 0:
                G.add_edge(g.vertex_data[u], g.vertex_data[v], weight=g.adj_matrix[u][v])

    # Draw the graph
    pos = nx.spring_layout(G, seed=42, k=0.1)
    plt.figure(figsize=(15, 8))
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightgreen')
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='black')

    # Find the shortest route
    for i in range(g.size):
        if distances[i] != float('inf') and previous[i] is not None:
            path = g.reconstruct_path('A', g.vertex_data[i], previous)
            edges_in_path = [(path[j], path[j+1]) for j in range(len(path)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, width=3, edge_color='lightblue')

    # Edge labels with weights
    edge_labels = {(g.vertex_data[u], g.vertex_data[v]): g.adj_matrix[u][v]
                   for u in range(g.size) for v in range(g.size) if g.adj_matrix[u][v] != 0}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)


    # Initialize Table
    table_data = []
    for i, d in enumerate(distances):
        table_data.append([g.vertex_data[i], d])

    # Display the table
    plt.table(cellText=table_data, colLabels=["Vertex", "Shortest Distance"],
            loc='best', cellLoc='center', colColours=["#f0f0f0"]*2, 
            bbox=[0.7, 0.1, 0.25, 0.8])

    # Displaying Graph
    plt.title("Graph Visualization with Dijkstra's Shortest Paths from 'F'")
    plt.axis('off')
    plt.show()

def main():
    graph = initGraph()
    initVisual(graph, 'F')

if __name__ == "__main__":
    main()
