"""Depth-First Search.
   Better memory complexity than Breadth-First Search.
   Can be implemented recursively or through iteration."""


class Node:
    def __init__(self, data, *neighbors):
        self.data = data
        self.neighbors = neighbors
        self.visited = False


def dfs_recursion(node):
    node.visited = True
    print(node.data)

    for neighbor in node.neighbors:
        if not neighbor.visited:
            dfs_recursion(neighbor)


def dfs_iteration(node):
    stack = []
    stack.append(node)

    while stack != []:
        actual_node = stack.pop()
        print(actual_node.data)
        actual_node.visited = True

        for neighbor in actual_node.neighbors[::-1]:
            if neighbor.visited is False:
                stack.append(neighbor)


if __name__ == "__main__":
    node8 = Node("H")
    node7 = Node("G", node8)
    node6 = Node("F")
    node5 = Node("E")
    node4 = Node("D", node5)
    node3 = Node("C")
    node2 = Node("B", node3, node4)
    node1 = Node("A", node2, node6, node7)
    # dfs_recursion(node1)
    dfs_iteration(node1)
