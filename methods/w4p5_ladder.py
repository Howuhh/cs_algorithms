from math import inf


def max_ladder_sum(n, steps):
    D = [inf] * (n + 1)

    def max_rec(D, n):
        if D[n] == inf:
            if n == 0:
                D[n] = 0
            elif n == 1:
                D[n] = steps[0]
            else:
                D[n] = max(
                    max_rec(D, n - 1) + steps[n - 1],
                    max_rec(D, n - 2) + steps[n - 1],
                    )
        return D[n]
    
    return max_rec(D, n)


def max_ladder_sum_iter(n, steps):
    D = [0, 0] + steps

    for i in range(2, n + 2):
        D[i] = max(D[i - 1] + D[i], D[i - 2] + D[i])

    return D[n + 1]


def main():
    n = int(input())
    steps = [int(s) for s in input().split()]

    print(max_ladder_sum_iter(n, steps))


if __name__ == "__main__":
    main()