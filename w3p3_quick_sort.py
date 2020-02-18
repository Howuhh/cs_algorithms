import sys
import random


def partition(arr, l, r):
    x, j = arr[l], l

    for i in range(l + 1, r + 1):
        if arr[i] < x:
            j = j + 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[l], arr[j] = arr[j], arr[l]
    return j


def _quick_sort(arr, l, r):
    while l < r:
        # random partition for average O(nlogn) 
        swap_idx = random.randint(l, r)
        arr[l], arr[swap_idx] = arr[swap_idx], arr[l]

        m = partition(arr, l, r)

        # tail recursion elimination
        if abs(l - m) < abs(r - m):
            _quick_sort(arr, l, m - 1)
            l = m + 1
        else:
            _quick_sort(arr, m + 1, r)
            r = m - 1


def quick_sort(arr, key=None):
    sorted_arr = arr.copy()
    l, r = 0, len(arr) - 1

    _quick_sort(sorted_arr, l, r)

    return sorted_arr


# when there are a lot of equal elements in an array
def quick_sort_naive(arr):
    if not arr:
        return arr
    
    x = arr[len(arr) // 2]

    less = [el for el in arr if el < x]
    eq = [el for el in arr if el == x]
    greater = [el for el in arr if el > x]

    return quick_sort_naive(less) + eq + quick_sort_naive(greater)


def bisect_search(arr, item, on="end") -> int:
    assert on in ("end", "start")
    compare = (lambda x, y: x < y) if on == "end" else (lambda x, y: x <= y)
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if compare(arr[mid], item):
            left = mid + 1
        else:
            right = mid

    return left


def find_intersec(starts, ends, points):
    sorted_ends = quick_sort_naive(ends)  # O(nlogn)
    sorted_starts = quick_sort_naive(starts)  # O(nlogn)

    counts = []
    for point in points:  # O(m)
        count_end = bisect_search(sorted_ends, point, "end")  # O(logn)
        count_start = bisect_search(sorted_starts, point, "start")  # O(logn)
        counts.append(count_start - count_end)

    return counts  # O(nlogn) + O(mlogn) = O(nlogn + mlogn) = O(n + m) * O(logn)


def main():
    n, m = map(int, sys.stdin.readline().split())
    start = []
    end = []

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        start.append(a)
        end.append(b)

    points = list(map(int, sys.stdin.readline().split()))

    print(*find_intersec(start, end, points))


if __name__ == "__main__":
    main()