def fibanacci_head(n, accumulator=0):
    if n == 0:
        return 0
    if n == 1:
        return 1
    num1 = fibanacci_head(n - 1)
    num2 = fibanacci_head(n - 2)
    result = num1 + num2
    return result


def fibonacci_tail(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    print(f'num: {a + b}')
    return fibonacci_tail(n-1, b, a+b)


class Queens:
    def __init__(self, n):
        self.n = n
        self.chess_table = [[None for i in range(n)] for j in range(n)]

    def p(self):
        return self.chess_table


q = Queens(4)
q.p()
