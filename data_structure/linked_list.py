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
            return '[]'
        else:
            node = self.head
            while node.next_node is not None:
                lst.append(str(node.data))
                node = node.next_node
            lst.append(str(node.data))
        return f'[{", ".join(lst)}]'

    def add_start(self, data):
        # O(1)
        self.num_nodes += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_end(self, data):
        # O(n)
        self.num_nodes += 1
        new_node = Node(data)
        node = self.head

        if not self.head:
            self.head = new_node
        else:
            while node.next_node is not None:
                node = node.next_node
            node.next_node = new_node

    def del_head(self):
        # O(1)
        if not self.head:
            print("List is already empty.")
        else:
            self.num_nodes -= 1
            self.head = self.head.next_node

    def del_tail(self):
        # O(n)
        if not self.head:
            print("List is already empty.")
        elif not self.head.next_node:
            self.num_nodes -= 1
            self.head = None
        else:
            self.num_nodes -= 1
            node = self.head
            next = self.head.next_node
            while next.next_node is not None:
                node = next
                next = next.next_node
            node.next_node = None

    def list_size(self):
        # O(1)
        return self.num_nodes


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
    linked.del_head()
    print(linked)
    linked.del_tail()
    print(linked)
    linked.del_tail()
    linked.del_tail()
    linked.add_end(1)
    print(linked.list_size())
