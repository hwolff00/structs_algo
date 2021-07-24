"""Merge Sort.
   O(NlogN) linearithmic time"""


def merge_sort(items):
    # Divide Phase (split into single items)
    if len(items) == 1:  # base case
        return
    mid = len(items) // 2
    left_half = items[:mid]
    right_half = items[mid:]
    print(f'items: {items}')
    print(f'left: {left_half}')
    print(f'right: {right_half}')

    merge_sort(left_half)
    merge_sort(right_half)

    le = 0
    r = 0
    i = 0
    # Conquer Phase
    while le < len(left_half) and r < len(right_half):
        if left_half[le] < right_half[r]:
            items[i] = left_half[le]
            le += 1
        else:
            items[i] = right_half[r]
            r += 1
        i += 1

    while le < len(left_half):
        items[i] = left_half[le]
        le += 1
        i += 1
    while r < len(right_half):
        items[i] = right_half[r]
        r += 1
        i += 1
    return items


if __name__ == "__main__":
    print(merge_sort([1, 5, 7, 3, 4, 9, 12, 2]))
