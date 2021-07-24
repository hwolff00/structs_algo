"""Bubble Sort.
   This is my life now. Why has my creator chosen this for me? Why have I
   chosen this for myself?
   O(N^2) quadratic runtime"""


class BubbleSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        for i in range(len(self.nums)-1):
            for j in range(len(self.nums)-i-1):
                if self.nums[j] > self.nums[j+1]:
                    self.swap(j, j+1)
        return self.nums

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


if __name__ == "__main__":
    b = BubbleSort([2, 7, 3, 9, 1])
    print(b.sort())
