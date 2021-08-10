# def is_edgecase(x: float, y: int):
#     if x == 0:
#         return 0
#
#     if x < 0 or y < 0:
#         print("Negative numeric input is not allowed. Answer will be 0.")
#         return 0
#     return 1
#
#
# def root(x: float, y: int) -> float:
#     """O(logN) run time bc binary search logarthmic run time.
#     O(1) constant memory bc as the numbers grow higher, the memory
#     stays constant"""
#
#     if is_edgecase(x, y) == 0:
#         return 0
#
#     lower = 0
#     upper = max(1, x)
#     root = (upper + lower) / 2
#     while root - lower >= 0.001:
#         if (root ** y) > x:
#             upper = root
#         elif (root ** y) < x:
#             lower = root
#         else:
#             break
#         root = (upper + lower) / 2
#     return round(root, 3)
#
#
# if __name__ == "__main__":
#     print(root(8.0, 2))
#     print(root(7.0, -3))


"""What we do is pick a number between 0 and x and see if num ** y
is greater than x (too high) or less than x (too low), we then reset to only
search that half of our range"""


def quicksort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [num for num in arr[1:] if num < pivot]
        right = [num for num in arr[1:] if num > pivot]
        pivot = [pivot]
        return quicksort(left) + pivot + quicksort(right)
    return arr


print(quicksort([0, 5, 4, 3, 2, 6]))
print(quicksort([10, 5, 44, 223, 2, 56]))
