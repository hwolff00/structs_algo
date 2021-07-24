"""Merge Sort.
   O(NlogN) linearithmic time"""


def merge_sort(items):
    if len(items) == 1:
        return
    mid = len(items) // 2
    left_half = items[:mid]
    right_half = items[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            items[k] = left_half[i]
            i += 1
        else:
            items[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        items[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        items[k] = right_half[j]
        j += 1
        k += 1
    return items


if __name__ == "__main__":
    print(merge_sort([1, 5, 7, 3, 4, 9, 12, 2]))
