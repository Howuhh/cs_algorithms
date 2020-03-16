import sys


def children(node):
    left, right = 2*node + 1, 2*node + 2
    return left, right


def shift_down(heap, node, log):
    left, right = children(node)

    # heap bound check
    if left >= len(heap):
        return
    elif right >= len(heap):
        left, right = left, left

    child_v, child_idx = min((heap[left], left), (heap[right], right))

    if heap[node] > child_v:
        log.append((node, child_idx))

        heap[node], heap[child_idx] = heap[child_idx], heap[node]
        shift_down(heap, child_idx, log)


def heapify(arr):
    n = len(arr)
    log = []

    for i in range(n // 2, -1, -1):
        shift_down(arr, i, log)
    
    return log


def main():
    n = int(input())
    arr = [int(x) for x in sys.stdin.readline().split()]
    log = heapify(arr)

    print(len(log))
    for parent, child in log:
        print(parent, child)


if __name__ == "__main__":
    main()