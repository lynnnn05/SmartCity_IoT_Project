"""
Module: app_gui.py
Description: The Tkinter GUI Presentation layer. 
             Follows MVC architecture by decoupling UI from algorithm logic.
"""
import tkinter as tk
from navigator_logic import HKMapGraph

class NavigatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task 2: HK Ambulance Smart Navigator (Graph & Dijkstra)")
        self.root.geometry("650x650") 
        self.root.configure(bg="#F4F7F9")
        
        self.hk_map = HKMapGraph()
        self._setup_network()
        
        self._build_ui()
        self.draw_map()

    def _build_ui(self):
        """Constructs the dashboard interface."""
        # Header
        tk.Label(self.root, text="📍 HK Emergency Routing System", 
                 font=("Segoe UI", 16, "bold"), bg="#F4F7F9", fg="#004B87").pack(pady=(15, 5))
                 
        # Graph Canvas
        self.canvas = tk.Canvas(self.root, width=580, height=420, bg="white", highlightthickness=2, highlightbackground="#DDDDDD")
        self.canvas.pack(pady=10)
        
        # Control Panel
        btn_frame = tk.Frame(self.root, bg="#F4F7F9")
        btn_frame.pack()
        
        tk.Button(btn_frame, text="🚑 Dispatch Ambulance to QMH", 
                  command=self.run_navigation, bg="#D32F2F", fg="white", 
                  font=("Segoe UI", 11, "bold"), padx=15, pady=8, cursor="hand2").pack(pady=10)

        self.lbl_info = tk.Label(self.root, text="System Ready. Waiting for dispatch command...", 
                                 bg="#F4F7F9", font=("Segoe UI", 11), justify="center")
        self.lbl_info.pack()

    def _setup_network(self):
        """
        Builds the graph with strategic 'traps' to prove algorithm robustness.
        """
        # TRAP 1: The Direct Route (Looks obvious, but heavily congested)
        self.hk_map.add_edge("Central", "Queen Mary Hospital", 40) 
        
        # TRAP 2: The Greedy Trap (Fastest initial step, but leads to a bottleneck)
        self.hk_map.add_edge("Central", "Pok Fu Lam", 5)
        self.hk_map.add_edge("Pok Fu Lam", "Queen Mary Hospital", 30) # Total 35m
        
        # THE GLOBAL OPTIMUM: Requires more stops, but yields the shortest time
        self.hk_map.add_edge("Central", "Wan Chai", 8)
        self.hk_map.add_edge("Wan Chai", "Happy Valley", 7)
        self.hk_map.add_edge("Happy Valley", "Aberdeen", 10)
        self.hk_map.add_edge("Aberdeen", "Queen Mary Hospital", 6) # Total 31m
        
        # Extra connections for graph complexity
        self.hk_map.add_edge("Pok Fu Lam", "Aberdeen", 20)

    def draw_map(self, highlight_path=[]):
        """Renders the nodes and edges, highlighting the calculated shortest path."""
        self.canvas.delete("all")
        coords = self.hk_map.coordinates
        
        # 1. Draw Edges (Roads)
        for u in self.hk_map.graph:
            for v, w in self.hk_map.graph[u]:
                x1, y1 = coords[u]
                x2, y2 = coords[v]
                
                # Check if this edge is part of the optimal path
                is_optimal = False
                if u in highlight_path and v in highlight_path:
                    if abs(highlight_path.index(u) - highlight_path.index(v)) == 1:
                        is_optimal = True
                        
                color = "#E53935" if is_optimal else "#E0E0E0"
                width = 4 if is_optimal else 2
                self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
                
                # Draw Weights (Time in minutes) with an offset box for readability
                mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                self.canvas.create_rectangle(mid_x-12, mid_y-8, mid_x+12, mid_y+8, fill="white", outline="")
                self.canvas.create_text(mid_x, mid_y, text=f"{w}m", fill="#555555", font=("Consolas", 9, "bold"))
        
        # 2. Draw Nodes (Locations)
        for node, (x, y) in coords.items():
            color = "#004B87" if node in highlight_path else "#757575"
            size = 9 if node in highlight_path else 6
            self.canvas.create_oval(x-size, y-size, x+size, y+size, fill=color, outline=color)
            
            # Draw Labels
            text_y_offset = -18 if y > 150 else 18 # Prevent text from going off-screen
            self.canvas.create_text(x, y+text_y_offset, text=node, font=("Segoe UI", 10, "bold"), fill=color)

    def run_navigation(self):
        """Triggers the algorithm and updates the UI with the result."""
        path, time = self.hk_map.dijkstra("Central", "Queen Mary Hospital")
        self.draw_map(path)
        
        result_text = (f"✅ ALGORITHM SUCCESS: Global Optimum Found\n\n"
                       f"Shortest Time: {time} minutes\n"
                       f"Optimal Path: {' ➔ '.join(path)}")
        self.lbl_info.config(text=result_text, fg="#004B87", font=("Segoe UI", 11, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = NavigatorGUI(root)
    root.mainloop()