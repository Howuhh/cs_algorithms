import random

# https://rcoh.me/posts/linear-time-median-finding/
# https://stepik.org/lesson/13250/step/1?unit=3435

# A[l...m1] < x, A[m1 + 1 ...m2] == x, A[m2+1...r] > x
# Чтобы понять что происходит - нарисовать на бумажке для [4, 2, 8, 6, 4, 1, 5, 9 7]
# Чтобы апдейтнуть если одинаковые, меняем то, что меньше с первым что больше,
# а потом меняем это с одинаковым + апдейтим индекс
# в конце меняем одинакове с теми что меньше
def partition(A, l, r):
    m1, m2 = l, l

    for k in range(l + 1, r + 1):        
        if A[k] < A[l]:
            m1 = m1 + 1
            A[m1], A[k] = A[k], A[m1]
        elif A[k] == A[l]:
            A[m1], A[m1 + 1] = A[m1 + 1], A[m1]
            A[m1], A[k] = A[k], A[m1]
            m1 = m1 + 1
            m2 = m2 + 1

    # check for equal elements swap
    if abs(l - m2) >= 1:
        for i in range(m2 + 1):
            A[i], A[m1 - i] = A[m1 - i], A[i]
        return m2, m1
    else:
        A[m2], A[m1] = A[m1], A[m2]
        return m1, m2

def quickselect(A, l, r, k):
    random_idx = random.randint(l, r)
    A[l], A[random_idx] = A[random_idx], A[l]
    # mid = (l + r) // 2
    # A[l], A[mid] = A[mid], A[l]

    m1, m2 = partition(A, l, r)

    if l == m1 == m2 == r:
        return A[r]
    elif m1 + 1 <= k <= m2:
        return A[m1 + 1]
    elif l <= k <= m1:
        return quickselect(A, l, m1, k)
    else:
        return quickselect(A, m2 + 1, r, k)


def median(arr):
    A, k = arr.copy(), len(arr) // 2
    if len(arr) % 2 == 1:
        return quickselect(A, 0, len(arr) - 1, k)
    else:
        return (quickselect(A, 0, len(arr) - 1, k) + quickselect(A, 0, len(arr) - 1, k - 1)) / 2


if __name__ == "__main__":
    test = [8, 2, 11, 6, 3, 1, 4, 5, 9, 7, 12] 

    print(sorted(test))
    print(median(test))



# more easy to write, but not inplace
def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect_naive(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect_naive(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect_naive(l, len(l) / 2, pivot_fn))


def quickselect_naive(l, k, pivot_fn):
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect_naive(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect_naive(highs, k - len(lows) - len(pivots), pivot_fn)