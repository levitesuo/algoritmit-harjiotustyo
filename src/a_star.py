from heapq import heappop, heappush
from heurestic_function import heurestic_function
from node import Node


def find_path(goal, nodes, size):
    path = [(goal//size, goal % size)]
    parent = nodes[goal].parent
    while parent != None:
        path.append((parent//size, parent % size))
        parent = nodes[parent].parent
    return {'path': path, 'cost': nodes[goal].g}


def a_star(start_cord, goal_cord, grid, h_func=heurestic_function):
    size = len(grid)
    start = start_cord[0]*size + start_cord[1]
    goal = goal_cord[0] * size + goal_cord[1]
    closed_list = [False for i in range(size ** 2)]
    open_list = []
    nodes = [Node((i//size, i % size), grid)
             for i in range(size ** 2)]

    nodes[start].g = 0
    heappush(open_list, (0, start))
    while len(open_list) != 0:
        g, p = heappop(open_list)
        closed_list[p] = nodes[p].f
        for edge in nodes[p].fedges:
            cost, np = edge
            if not closed_list[np]:
                if goal == np:
                    nodes[np].g = cost + g
                    nodes[np].parent = p
                    result = find_path(goal, nodes, size)
                    result['closed'] = closed_list
                    result['cost'] = new_g
                    return result
                new_g = cost + g
                h = h_func(grid, np, goal)
                if h:
                    with open("logfile.txt", "a") as file:
                        file.write(
                            f"\nnew_g - {new_g}\tg - {g}\tcost - {cost}")
                new_f = h + new_g
                if nodes[np].f == float('inf') or nodes[np].f > new_f:
                    heappush(open_list, (new_f, np))
                    nodes[np].f = new_f
                    nodes[np].g = new_g
                    nodes[np].parent = p
    return False
