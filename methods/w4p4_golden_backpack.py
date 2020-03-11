from math import inf
from w4p3_editing_distance import print_array


def max_knapsack_norep(W, weights, costs=None):
    n = len(weights)
    D = [[0] * (n + 1) for _ in range(W + 1)]

    # init weights
    for w in range(W + 1):
        D[w][0] = 0

    # init for items
    for i in range(n + 1):
        D[0][i] = 0

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            D[w][i] = D[w][i - 1]  # just keep prev items
            
            # what item we can add to max weight
            w_i = weights[i - 1]
            if w_i <= w:
                D[w][i] = max(D[w][i], D[w - w_i][i - 1] + w_i)

    print_array(D)

    return D[W][n]


def main():
    W, n = map(int, input().split())
    weights = [int(w) for w in input().split()]

    max_weight = max_knapsack_norep(W, weights)
    print(max_weight)


if __name__ == "__main__":
    main()