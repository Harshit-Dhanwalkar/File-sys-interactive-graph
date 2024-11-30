import json

import matplotlib
import matplotlib.pyplot as plt
import networkx as nx

# Use the TkAgg backend for interactive plotting
matplotlib.use("Agg")


def load_graph_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def visualize_graph(graph_data):
    G = nx.DiGraph()  # Directed graph to represent relationships

    # Add nodes
    for node in graph_data["nodes"]:
        G.add_node(node["id"], label=node["label"], group=node["group"])

    # Add edges
    for edge in graph_data["edges"]:
        G.add_edge(edge["from"], edge["to"], relation=edge["relation"])

    # Extract labels for nodes
    labels = {node["id"]: node["label"] for node in graph_data["nodes"]}

    # Draw the graph
    pos = nx.spring_layout(G)  # Layout algorithm
    nx.draw(
        G,
        pos,
        labels=labels,  # Use custom labels
        with_labels=True,
        node_size=3000,
        node_color="lightblue",
        font_size=10,
    )

    # Save and show the plot
    plt.savefig("graph_plot.png")  # Save the plot as an image
    print("Graph plot saved as 'graph_plot.png'")
    plt.show()


if __name__ == "__main__":
    file_path = input("Enter the path to the graph data JSON file: ")
    graph_data = load_graph_data(file_path)
    print("Graph data loaded successfully!")
    visualize_graph(graph_data)
