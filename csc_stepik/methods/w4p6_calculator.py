from math import inf


def argmin(arr):
    return min(enumerate(arr), key=lambda tup: tup[1])


# rec limit exceeded
def min_calc_operations(n):
    D = [inf] * (n + 1)
    
    def min_calc(n):
        if D[n] == inf:
            if n <= 1:
                D[n] = 0
            else:
                D[n] = min(
                    min_calc(n // 2) if n % 2 == 0 else inf,
                    min_calc(n // 3) if n % 3 == 0 else inf,
                    min_calc(n - 1)) + 1
        return D[n]

    return min_calc(n) 


def min_calc_operations_iter(n, return_h=False):
    D, prev = [inf] * (n + 1), [-1] * (n + 1)

    D[1] = 0
    for i in range(2, n + 1):
        div2 = i // 2 if i % 2 == 0 else 0  # D[0] = inf
        div3 = i // 3 if i % 3 == 0 else 0
        sub1 = i - 1
        
        indx, min_op = argmin([D[div2], D[div3], D[sub1]])

        D[i] = min_op + 1
        prev[i] = [div2, div3, sub1][indx]

    if return_h:
        return D[n], prev

    return D[n]


def backtrack_calc(prev):
    last = len(prev) - 1
    seq = [last]

    while last > -1:
        seq.append(prev[last])
        last = prev[last]

    return seq[::-1][1:]


def test():
    assert min_calc_operations(1) == 0
    assert min_calc_operations(2) == 1
    assert min_calc_operations(3) == 1
    assert min_calc_operations(4) == 2
    assert min_calc_operations(5) == 3
    assert min_calc_operations(6) == 2

    assert min_calc_operations_iter(1) == 0
    assert min_calc_operations_iter(2) == 1
    assert min_calc_operations_iter(3) == 1
    assert min_calc_operations_iter(4) == 2
    assert min_calc_operations_iter(5) == 3
    assert min_calc_operations_iter(6) == 2



def main():
    n = int(input())
    min_k, prev = min_calc_operations_iter(n, True)

    print(min_k)
    print(*backtrack_calc(prev))


if __name__ == "__main__":
    main()
    test()