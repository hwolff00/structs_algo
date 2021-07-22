"""Basic Binary Search Tree."""
# insert, traversal (three ways), removal


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data, None)
            return self.root.data
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if not node.left_child:
                node.left_child = Node(data, node)
                print(f"{node.left_child.data}: left child of {node.data}.")
            else:
                self.insert_node(data, node.left_child)
        else:
            if not node.right_child:
                node.right_child = Node(data, node)
                print(f"{node.right_child.data}: right child of {node.data}.")
            else:
                self.insert_node(data, node.right_child)
# base case = if lower, no left leaf. if higher, no right leaf


if __name__ == "__main__":
    tree = BST()
    print(tree.insert(6))
    tree.insert(4)
