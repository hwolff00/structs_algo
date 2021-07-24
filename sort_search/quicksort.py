"""Quicksort.
   Average O(NlogN) linearithmic --considered faster than merge sort."""


class QuickSort:
    # Partitioning phase- chose random num in array as pivot value
    def __init__(self, items):
        self.items = items

    def sort(self):
        self.quick_sort(0, len(self.items)-1)  # Range of values
        return self.items

    def quick_sort(self, low, high):
        if low >= high:
            return
        pivot = self.partition(low, high)
        self.quick_sort(low, pivot - 1)
        self.quick_sort(pivot + 1, high)

    def partition(self, low, high):
        pivot = (low + high) // 2
        self.items[pivot], self.items[high] = self.items[high], self.items[pivot]

        for idx in range(low, high):
            if self.items[idx] <= self.items[high]:
                self.items[low], self.items[idx] = self.items[idx], self.items[low]
                low += 1
        self.items[low], self.items[high] = self.items[high], self.items[low]
        return low


if __name__ == "__main__":
    q = QuickSort([1, 5, 6, 9, 3, 10, 7, 543])
    print(q.sort())
