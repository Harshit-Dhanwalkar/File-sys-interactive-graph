```markdown
# Interactive File Graph Visualization

This project scans a directory and generates a visual representation of its file structure as a graph. It provides two components:
1. **Graph Data Generation**: Extracts file and directory relationships and stores them in a JSON file.
2. **Interactive Visualization**: Visualizes the generated graph using Python libraries. Nodes can be made interactive to open files directly in their default applications.

## Features

### 1. Graph Data Generation
- **Script**: `directory_scanner.py`
- **Functionality**:
  - Scans a directory recursively.
  - Extracts tags (e.g., `#tag`) from text-based files.
  - Represents directories and files as nodes and their relationships as edges.
  - Outputs the graph data as a JSON file.

### 2. Visualization
- **Script**: `visualize_graph.py`
- **Functionality**:
  - Reads the JSON graph data.
  - Visualizes the file structure using NetworkX and Plotly.
  - Nodes are labeled with filenames or directory names (not full paths).
  - **Interactive Feature (Future Development)**: Makes nodes clickable to open files using `xdg-open`.

### Outputs
- `graph_data.json`: Contains the graph's structure (nodes and edges).
- `graph_plot.png`: Static visualization of the graph.
- **Interactive Graph** (under development): A browser-based interface with clickable nodes.

---

## How to Use

### Prerequisites
- Python 3.7+
- Install required libraries:
  ```bash
  pip install networkx matplotlib plotly
  ```

### Steps
1. **Generate Graph Data**:
   Run the directory scanner script:
   ```bash
   python directory_scanner.py
   ```
   - Enter the path to the directory you want to scan.
   - The script will save `graph_data.json` in the current directory.

2. **Visualize the Graph**:
   Static plot:
   ```bash
   python visualize_graph.py
   ```
   - Enter the path to `graph_data.json`.
   - The script will save a static plot as `graph_plot.png`.

   Interactive visualization (under development):
   ```bash
   python interactive_visualize_graph.py
   ```
   - Opens an interactive browser-based graph. (Work in progress)

---

## Project Structure
```
.
├── directory_scanner.py         # Script for scanning directories and generating graph data
├── visualize_graph.py           # Script for static graph visualization
├── interactive_visualize_graph.py # Script for interactive graph visualization (future development)
├── graph_data.json              # Example output from the directory scanner
├── graph_plot.png               # Example static graph plot
├── README.md                    # Project documentation
```

---

## Future Development

### 1. Interactive Graph with Clickable Nodes
- **Goal**: Make graph nodes clickable to open files using `xdg-open`.
- **Approach**:
  - Use `Plotly` for interactive graph rendering.
  - Implement click event handlers to execute system commands.

### 2. Advanced Tag Extraction and Filtering
- Add support for customizable tag patterns.
- Allow filtering nodes based on specific tags.

### 3. Improved Layout and Styling
- Enhance the layout for better readability of large graphs.
- Add support for color-coding nodes based on file types or tags.

### 4. Standalone Web Application
- Create a fully interactive web app using frameworks like Dash or Flask.
- Provide additional features like search, filter, and export.

### 5. Cross-Platform Support
- Ensure compatibility with both Linux (`xdg-open`) and other platforms (e.g., Windows `start` and macOS `open`).

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for bug fixes, enhancements, or new features.

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.
```

This README explains the project, guides users on usage, and outlines future developments, including making the graph interactive. You can adapt the content as necessary. File-sys-interactive-graph
