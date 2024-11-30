import json
import os
import re
from pathlib import Path


def scan_directory(root_dir):
    graph_data = {"nodes": [], "edges": []}

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Add a node for the directory itself
        dir_node = {
            "id": dirpath,
            "label": os.path.basename(dirpath),
            "group": "directory",
            "tags": [],
        }
        if dir_node not in graph_data["nodes"]:
            graph_data["nodes"].append(dir_node)

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            tags = extract_tags(file_path)
            node = {"id": file_path, "label": filename, "group": "file", "tags": tags}
            graph_data["nodes"].append(node)

            # Add directory relationship
            graph_data["edges"].append(
                {"from": dirpath, "to": file_path, "relation": "contains"}
            )

    return graph_data


def extract_tags(file_path):
    tags = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()
            tags = [tag.strip() for tag in re.findall(r"#(\w+)", content)]
    except Exception as e:
        print(f"Could not read file {file_path}: {e}")
    return tags


# Save the graph data as a JSON file
def save_graph_data(graph_data, output_path="graph_data.json"):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(graph_data, f, indent=4)


# Example usage
if __name__ == "__main__":
    directory_to_scan = input("Enter the directory path to scan: ")
    graph_data = scan_directory(directory_to_scan)
    save_graph_data(graph_data)
    print("Graph data saved to graph_data.json")
