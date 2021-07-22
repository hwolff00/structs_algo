"""Basic Binary Search Tree."""
# insert, traverse (three ways), search, remove


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

    def in_order_traversal(self):
        """Prints out bst values in sorted order."""
        if not self.root:
            return "Tree is empty."
        self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)
        print(node.data)
        if node.right_child:
            self.traverse_in_order(node.right_child)

    def pre_order_traversal(self):
        """Helpful for copying the bst tree:
        (ie if add these to new bst, it will be an identical copy)."""
        if not self.root:
            return "Tree is empty."
        self.traverse_pre_order(self.root)

    def traverse_pre_order(self, node):
        if node:
            print(node.data)
            self.traverse_pre_order(node.left_child)
            self.traverse_pre_order(node.right_child)

    def post_order_traversal(self):
        """Helpful for deleting all nodes from tree."""
        if not self.root:
            return "Tree is empty."
        self.traverse_post_order(self.root)

    def traverse_post_order(self, node):
        if node.left_child:
            self.traverse_post_order(node.left_child)
        if node.right_child:
            self.traverse_post_order(node.right_child)
        print(node.data)

    def search_bst(self, data):
        if not self.root:
            return "Tree is empty."
        node = self.root
        while True:
            if data == node.data:
                return "Node in tree!"
            elif data < node.data and node.left_child:
                node = node.left_child
            elif data > node.data and node.right_child:
                node = node.right_child
            else:
                return "Node not in tree."

    def remove(self, data):
        if not self.root:
            return "Tree is empty."
        node = self.root
        self.remove_node(data, node)

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)
        return node

    def remove_node(self, data, node):
        if node is None:
            print(f"Node {data} not in tree")
            return
        elif data < node.data:
            self.remove_node(data, node.left_child)
        elif data > node.data:
            self.remove_node(data, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                print(f"Removing leaf node {node.data}")
                if node.parent is not None and node.parent.left_child == node:
                    node.parent.left_child = None
                elif node.parent is None:
                    self.root = None
                else:
                    node.parent.right_child = None
            elif not node.left_child and node.right_child is not None:
                print(f"Removing {node.data}: has single right child.")
                if node.parent.left_child == node:
                    node.parent.left_child = node.right_child
                elif node.parent is None:
                    self.root = node.right_child
                else:
                    node.parent.right_child = node.right_child
            elif node.left_child is not None and not node.right_child:
                print(f"Removing {node.data}: has single left child.")
                if node.parent.right_child == node:
                    node.parent.right_child = node.left_child
                elif node.parent is None:
                    self.root = node.left_child
                else:
                    node.parent.left_child = node.left_child
            else:
                print(f"Removing {node.data}: has left and right child.")
                predecessor = self.get_predecessor(node.left_child)
                temp_node = predecessor.data
                predecessor.data = node.data
                node.data = temp_node
                self.remove_node(data, predecessor)


if __name__ == "__main__":
    tree = BST()
    print(tree.insert(6))
    tree.insert(4)
    tree.insert(9)
    tree.insert(5)
    tree.insert(12)
    tree.insert(13)
    tree.insert(2)
    tree.in_order_traversal()
    # tree.post_order_traversal()
    tree.remove(4)
    tree.remove(9)
    tree.in_order_traversal()
