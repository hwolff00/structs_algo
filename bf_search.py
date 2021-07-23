from collections import deque  # doubly ended queue

"""Breadth-First Search."""
"""Can be used for Dijikstra's algorithm, Edmonds-Karp algorithm,
   Cheyen's algorithm or for AI surroundings exploration."""


class Node:
    def __init__(self, data, *neighbors: []):
        self.data = data
        self.adjacency_list = neighbors
        self.visited = False


def breath_first_search(start_node):
    queue = deque([start_node])

    while queue:
        # Remove first item of queue
        actual_node = queue.popleft()
        actual_node.visited = True
        print(actual_node.data)

        for node in actual_node.adjacency_list:
            if not node.visited:
                queue.append(node)


if __name__ == "__main__":
    node5 = Node("E")
    node3 = Node("C")
    node4 = Node("D", node5)
    node2 = Node("B", node4)
    node1 = Node("A", node2, node3)
    breath_first_search(node1)
