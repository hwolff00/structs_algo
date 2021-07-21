"""Working with linked list data type."""


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.num_nodes = 0

    def __str__(self):
        lst = []
        if not self.head:
            return f'[]'
        else:
            node = self.head
            while node.next_node is not None:
                lst.append(str(node.data))
                node = node.next_node
            lst.append(str(node.data))
        return f'[{", ".join(lst)}]'

    def add_start(self, data):
        self.num_nodes += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_end(self, data):
        self.num_nodes += 1
        new_node = Node(data)
        node = self.head

        if not self.head:
            self.head = new_node
        else:
            while node.next_node is not None:
                node = node.next_node
            node.next_node = new_node


if __name__ == "__main__":
    linked = LinkedList()
    print(linked)
    linked.add_end(4)
    linked.add_start(5)
    linked.add_end(7)
    print(linked)
    new = LinkedList()
    new.add_end(19)
    print(new)
    print(linked)
