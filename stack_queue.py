"""Stacks and Queues."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.head = None
        self.popped = None

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
        if not self.head:
            return True
        return False

    def peek(self):
        if not self.head:
            self.head = self.popped
        else:
            self.popped.next_node = self.head
            self.head = self.popped
            self.popped = None


if __name__ == "__main__":
    pringles = Stack()
    print(pringles.is_empty())
    pringles.push(4)
    pringles.push(7)
    print(pringles.pop())
    print(pringles.pop())
    pringles.peek()
    print(pringles.is_empty())
