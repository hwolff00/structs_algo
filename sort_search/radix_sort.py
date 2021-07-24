"""LSD (least significant digit) Radix sort. aka right to left.
   Non-comparison based int/str sort"""


class RadixSort:
    def __init__(self, data, size=10):
        self.data = data
        self.size = size

    def get_digits(self):
        return len(str(max(self.data)))

    def sort(self):
        for digit in range(self.get_digits()):
            self.counting_sort(digit)
        return self.data

    def counting_sort(self, digits):
        count_lis = [[] for _ in range(self.size)]
        for num in self.data:
            index = (num // (10 ** digits)) % 10
            count_lis[index].append(num)

        d = 0

        for i in range(len(count_lis)):
            while len(count_lis[i]) > 0:
                self.data[d] = count_lis[i].pop(0)
                d += 1


if __name__ == "__main__":
    r = RadixSort([1234, 5555, 913567, 123])
    print(r.sort())
