from math import inf

# https://strncat.github.io/jekyll/update/2019/06/25/longest-increasing-subsequence.html
def lis_nlogn(seq):
    k, M = 1, [-1] + [inf] * len(seq)
    prev = [-1] * len(seq)

    M[1] = 0
    for i in range(1, len(seq)):
        if seq[i] >= seq[M[k]]:
            k = k + 1
            M[k] = i

            prev[M[k]] = M[k - 1]
        else:
            # bisect for M[j - 1] < i <= M[j]
            left, right = 1, k
            while left < right:
                mid = (left + right) // 2

                if seq[M[mid]] <= seq[i]:
                    left = mid + 1
                else:
                    right = mid
            M[left] = i
            prev[M[left]] = M[left - 1]


    new_seq = []
    index = M[k]
    while index != -1:
        new_seq.append(index)
        index = prev[index]
    # print(new_seq)

    return k, new_seq[::-1]


def main_stepick():
    n = int(input())
    seq = list(map(lambda x: int(x) * -1, input().split()))

    k, idxs = lis_nlogn(seq)
    print(k)
    print(*[i + 1 for i in idxs])


def test():
    test = [-5, -3, -4, -4, -2]
    # test = [-9, -8, -7, -7, 2, 3, 5, -6]
    # test1 = [1, 1, 1, 1]
    # test_lis = [3, 8, 1, 2, 7, 9, 6, 4, 5]
    r = len(test)

    k, idxs = lis_nlogn(test)
    print(k)
    print(*[i + 1 for i in idxs[1:k+1]])


if __name__ == "__main__":
    # test()
    # main()
    main_stepick()