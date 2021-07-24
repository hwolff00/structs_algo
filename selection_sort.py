"""Selection Sort.
   O(N^2)"""


def selection_sort(items):
    for idx, _ in enumerate(items):
        index = idx
        for j in range(idx, len(items)):
            if items[j] < items[index]:
                index = j
        if index != idx:
            items[idx], items[index] = items[index], items[idx]

    return items


if __name__ == "__main__":
    print(selection_sort([1, 5, 3, 9, 12, 4]))
    print(selection_sort([1.5, 5, 3, -9, 12, 4, 120]))
