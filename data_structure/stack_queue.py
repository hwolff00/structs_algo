"""Stacks and Queues."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.head = None
        self.popped = None

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

    def pop(self):
        if not self.head:
            return "Stack is already empty."
        else:
            self.popped = self.head.data
            self.head = self.head.next_node
            return self.popped

    def push(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node

    def is_empty(self):
        return not self.head

    def peek(self):
        if not self.head:
            self.head = self.popped
        else:
            self.popped.next_node = self.head
            self.head = self.popped
            self.popped = None


class Queue:
    def __init__(self):
        self.head = None
        self.removed = None

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

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            head = self.head
            while head.next_node is not None:
                head = head.next_node
            head.next_node = node

    def remove(self):
        if not self.head:
            return "Queue empty."
        else:
            self.removed = self.head
            self.head = self.head.next_node
            return self.removed.data

    def peek(self):
        if not self.head:
            self.head = self.removed
        else:
            self.removed.next_node = self.head
            self.head = self.removed
            self.removed = None

    def is_empty(self):
        return not self.head


if __name__ == "__main__":
    pringles = Stack()
    print(pringles.is_empty())
    pringles.push(4)
    pringles.push(7)
    print(pringles)
    print(pringles.pop())
    print(pringles.pop())
    pringles.peek()
    print(pringles.is_empty())
    taco_truck = Queue()
    print(taco_truck.is_empty())
    taco_truck.add(4)
    taco_truck.add(7)
    print(taco_truck)
