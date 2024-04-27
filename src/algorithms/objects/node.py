class Node:
    def __init__(self, position, height, grid, height_mapping_function):
        self.position = position
        self.height = height
        self.parent = None
        self.edges = []

        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

        self._init_edges(grid, height_mapping_function)

    def _init_edges(self, grid, height_mapping_function):
        x = self.position[1]
        y = self.position[0]
        for i in range(3):
            for j in range(3):
                new_x = x + i - 1
                new_y = y + j - 1
                if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and not (i == 1 and j == 1):
                    if i - 1 != 0 and j - 1 != 0:
                        edge = height_mapping_function(
                            grid[new_y][new_x] - grid[y][x], len(grid)) * 1.42
                    else:
                        edge = height_mapping_function(
                            grid[new_y][new_x] - grid[y][x], len(grid))
                    self.edges.append((edge, new_x * len(grid) + new_y))
            self.edges = sorted(self.edges)