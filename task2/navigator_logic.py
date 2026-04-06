"""
Module: navigator_logic.py
Description: Core logic for the HK Smart Ambulance Navigator.
             Demonstrates the use of a Graph Data Structure (Adjacency List)
             and Dijkstra's Shortest Path Algorithm (Greedy strategy with global optimum).
"""
import sys

class HKMapGraph:
    """
    Represents the city map as a Weighted Graph.
    This goes beyond standard course materials (Trees/Lists) into Graph Theory.
    """
    def __init__(self):
        # Data Structure: Adjacency List using a Python Dictionary
        # Structure: {Node: [(Neighbor, Edge_Weight), ...]}
        # Space Complexity: O(V + E) where V is vertices, E is edges.
        self.graph = {}
        
        # UI Coordinates for rendering the Graph (x, y)
        self.coordinates = {
            "Central": (150, 80),
            "Pok Fu Lam": (100, 200),
            "Wan Chai": (300, 80),
            "Happy Valley": (350, 180),
            "Aberdeen": (280, 320),
            "Queen Mary Hospital": (100, 350)
        }

    def add_edge(self, u, v, weight):
        """
        Adds an undirected edge (bi-directional road) between two nodes.
        """
        if u not in self.graph: self.graph[u] = []
        if v not in self.graph: self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, start_node, end_node):
        """
        Algorithm: Dijkstra's Shortest Path.
        Time Complexity: O(V^2) with standard list, optimizable to O(E log V) with Min-Heap.
        Returns: (List of optimal path nodes, Total minimum time)
        """
        # Step 1: Initialization
        # Set all distances to infinity, except the start node (0)
        distances = {node: sys.maxsize for node in self.graph}
        distances[start_node] = 0
        
        predecessors = {node: None for node in self.graph}
        unvisited = list(self.graph.keys())

        # Step 2: Iterative Relaxation Process
        while unvisited:
            # Greedy Approach: Select the unvisited node with the smallest known distance
            current_node = min(unvisited, key=lambda node: distances[node])
            
            # If the smallest distance is infinity, remaining nodes are unreachable
            if distances[current_node] == sys.maxsize: 
                break
            # Optimization: Stop early if we reached the target destination
            if current_node == end_node: 
                break

            unvisited.remove(current_node)

            # Step 3: Edge Relaxation
            # Evaluate all neighbors of the current node to find shorter paths
            for neighbor, weight in self.graph[current_node]:
                new_path_dist = distances[current_node] + weight
                
                # If a shorter path is found, update the distance and predecessor
                if new_path_dist < distances[neighbor]:
                    distances[neighbor] = new_path_dist
                    predecessors[neighbor] = current_node

        # Step 4: Path Reconstruction (Backtracking from destination)
        path = []
        curr = end_node
        while curr is not None:
            path.insert(0, curr)
            curr = predecessors[curr]
            
        return path, distances[end_node]