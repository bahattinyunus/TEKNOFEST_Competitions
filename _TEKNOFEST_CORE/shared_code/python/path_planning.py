#!/usr/bin/env python3
"""
TEKNOFEST Elite Engineering Core
Path Planning (A* Search Algorithm)
"""

import heapq

class AStarPlanner:
    """
    Simple A* Path Planning algorithm for grid-based autonomous navigation.
    """
    
    def __init__(self, grid):
        self.grid = grid # 0: free, 1: obstacle
        self.rows = len(grid)
        self.cols = len(grid[0])
        
    def heuristic(self, a, b):
        """Manhattan distance heuristic."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
    def get_neighbors(self, pos):
        """Returns valid movement neighbors (4-way)."""
        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = pos[0] + dx, pos[1] + dy
            if 0 <= x < self.rows and 0 <= y < self.cols:
                if self.grid[x][y] == 0:
                    neighbors.append((x, y))
        return neighbors
        
    def plan(self, start, goal):
        """Finds the shortest path from start to goal."""
        open_list = []
        heapq.heappush(open_list, (0, start))
        
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}
        
        while open_list:
            _, current = heapq.heappop(open_list)
            
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1] # Reverse path
                
            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
                    
        return None # No path found

# --- Example Usage ---
if __name__ == "__main__":
    # 0 = Path, 1 = Wall
    map_grid = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    planner = AStarPlanner(map_grid)
    start_pos = (0, 0)
    goal_pos = (4, 4)
    
    print(f"📍 Calculating path from {start_pos} to {goal_pos}...")
    path = planner.plan(start_pos, goal_pos)
    
    if path:
        print(f"✅ Path found: {path}")
    else:
        print("❌ No path found!")
