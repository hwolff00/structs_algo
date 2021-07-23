"""Basic min and max heap.
   Applications: Dijkstra's algorithm and Prim's algorithm
   Created to implement heapsort
   Complete BST with O(1) max or min retreival"""

# Implementation with lists
capacity = 10


class ListMaxHeap:
    def __init__(self):
        self.heap_size = 0
        self.heap = [0] * capacity

    def insert(self, value):
        if self.heap_size == capacity:
            return "Heap is full."
        self.heap[self.heap_size] = value
        self.heap_size += 1

        self.heapify_up(self.heap_size - 1)

    def heapify_up(self, index):
        # idx * 2 + 1 = left_child
        # idx * 2 + 2 = right_child
        # (idx - 1) // 2 = parent (remainder guarentees parent)
        parent_index = (index - 1)//2
        if index > 0 and self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        largest_index = index
        if left_index < self.heap_size and self.heap[left_index] > self.heap[index]:
            largest_index = left_index
        if right_index < self.heap_size and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.heapify_down(largest_index)

    def get_max(self):
        return self.heap[0]

    def pull(self):
        "Return and remove max value."
        max_item = self.get_max()
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size -= 1
        self.heapify_down(0)
        return max_item

    def heap_sort(self):
        for _ in range(self.heap_size):
            max_item = self.pull()
            print(max_item)


class ListMinHeap:
    def __init__(self):
        self.heap_size = 0
        self.heap = [0] * capacity

    def insert(self, value):
        if self.heap_size == capacity:
            return "Heap is full."
        self.heap[self.heap_size] = value
        self.heap_size += 1

        self.heapify_up(self.heap_size - 1)

    def heapify_up(self, index):
        # idx * 2 + 1 = left_child
        # idx * 2 + 2 = right_child
        # (idx - 1) // 2 = parent (remainder guarentees parent)
        parent_index = (index - 1)//2
        if index > 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        smallest_index = index
        if left_index < self.heap_size and self.heap[left_index] < self.heap[index]:
            smallest_index = left_index
        if right_index < self.heap_size and self.heap[right_index] < self.heap[smallest_index]:
            smallest_index = right_index
        if index != smallest_index:
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            self.heapify_down(smallest_index)

    def get_min(self):
        return self.heap[0]

    def pull(self):
        "Return and remove min value."
        min_item = self.get_min()
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size -= 1
        self.heapify_down(0)
        return min_item

    def heap_sort(self):
        for _ in range(self.heap_size):
            min_item = self.pull()
            print(min_item)


if __name__ == "__main__":
    maximum = ListMaxHeap()
    for num in [5, 2, 12, 4, 16, 1]:
        maximum.insert(num)
    maximum.heap_sort()




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.parent = None
#         self.right_child = None
#         self.left_child = None
#
#
# class Min_Heap:
#     "Parent nodes are always <= their children."
#     def __init__(self):
#         self.root = None
#
#     def insert(self, data):
#         if not self.root:
#             self.root = Node(data)
#
#
#
#
# class Max_Heap:
#     "Parent nodes are always >= their children."
#     def __init__(self):
#         self.root = None
#
#     def insert(self, data):
#         if not self.root:
#             self.root = Node(data)
