# Not a part of the course, only my curiosity


def children(node):
    left, right = 2*node + 1, 2*node + 2
    return left, right


def shift_down(heap, node, size):
    left, right = children(node)

    # heap bound check
    if left >= size:
        return
    elif right >= size:
        left, right = left, left

    child_v, child_idx = max((heap[left], left), (heap[right], right))

    if heap[node] < child_v:
        heap[node], heap[child_idx] = heap[child_idx], heap[node]
        shift_down(heap, child_idx, size)


def heapify(arr):
    for i in range(len(arr) // 2, -1, -1):
        shift_down(arr, i, len(arr))


def partial_sort(arr, k):  # O(n + k*logn)
    "top k sort with heap sort"
    size = len(arr)
    heapify(arr)  # O(n)

    while size > len(arr) - k:  # O(k)
        print(arr)
        arr[0], arr[size - 1] = arr[size - 1], arr[0]
        size = size - 1
        shift_down(arr, 0, size)  # O(logn)


def heap_sort(arr):
    "inplace heap sort"
    size = len(arr)
    heapify(arr)   # Build heap O(n)

    while size > 0:  # O(n)
        print(arr)
        arr[0], arr[size - 1] = arr[size - 1], arr[0]
        size = size - 1
        shift_down(arr, 0, size)  # O(logn)


if __name__ == "__main__":
    test = [5, 4, 3, 2, 1]
    partial_sort(test, 2)

    print(test)