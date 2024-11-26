# Reference:
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
# https://www.geeksforgeeks.org/a-search-algorithm/

class Cell():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

ROW = COLUMN = 10

def astar(grid, start, end):
    # Grid Checking
    if not (0 <= start[0] < len(grid) and 0 <= start[1] < len(grid[0])):
        print("The starting point is outside the grid boundaries.")
        return []
    if not (0 <= end[0] < len(grid) and 0 <= end[1] < len(grid[0])):
        print("The destination point is outside the grid boundaries.")
        return []

    # Check if the cell are passable
    if grid[start[0]][start[1]] != 0:
        print("The starting point is blocked.")
        return []
    if grid[end[0]][end[1]] != 0:
        print("The destination point is blocked.")
        return []

    # Check if start equals end
    if start == end:
        print("Starting point is the same as the destination point.")
        return [start]

    # Create start and end nodes
    start_node = Cell(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Cell(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed lists
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # Generate children
        children = [
            Cell(current_node, (current_node.position[0] + dx, current_node.position[1] + dy))
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            if 0 <= current_node.position[0] + dx < len(grid) and
            0 <= current_node.position[1] + dy < len(grid[0]) and
            grid[current_node.position[0] + dx][current_node.position[1] + dy] == 0
        ]

        # Loop through children
        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

    # If the loop ends without finding a path
    print("No path found to the destination.")
    return []

def main():
    # 0 for open and 1 is for blocked
    grid = [
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

    start = (0, 0)
    end = (9, 9)

    path = astar(grid, start, end)

    if len(path) > 1:
        traced_path = " -> ".join([f"{node}" for node in path])
        print(f"Path: {traced_path}")
        print(f"Total Movement: {len(path) - 1}")

if __name__ == '__main__':
    main()
