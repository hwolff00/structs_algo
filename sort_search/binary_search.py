"""Binary Search.
   O(logN) time """


class BinarySearch:
    def __init__(self, nums):
        self.nums = nums
        self.phrase = ''

    def binary_search(self, search, nums=None):
        if nums is None:
            nums = self.nums

        mid = (len(nums)-1) // 2

        if len(nums) == 1 and nums[0] == search:
            self.phrase = f"{search} in list."
        elif len(nums) <= 1 and nums[0] != search:
            self.phrase = f"{search} not in list."
        elif search == nums[mid]:
            self.phrase = f"{search} in list!"
        elif search > nums[mid]:
            n = nums[mid+1:]
            self.binary_search(search, n)
        elif search < nums[mid]:
            n = nums[:mid]
            self.binary_search(search, n)
        return self.phrase


if __name__ == "__main__":
    b = BinarySearch([1, 2, 3, 5, 7, 9, 12, 15])
    for _ in [1, 2, 5, 6, 8, 0, 12, 15]:
        print(b.binary_search(_))
