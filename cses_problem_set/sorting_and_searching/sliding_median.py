import sys

from heapq import heappush, heappop, heappushpop, heapify
from heapq import _siftup, _siftdown

# https://stackoverflow.com/questions/15319561/how-to-implement-a-median-heap
def update_heaps(min_heap, max_heap, value):
    # if value > curr median -> min heap, else max heap
    heappush(max_heap, -heappushpop(min_heap, value))
    
    if len(max_heap) > len(min_heap):
        heappush(min_heap, -heappop(max_heap))


def get_median(min_heap, max_heap):
    if len(min_heap) > len(max_heap):
        return min_heap[0]
    else:
        return -max_heap[0]


def remove_from_heap(heap, value):
    # time limit due to this
    index = heap.index(value)

    heap[index], heap[-1] = heap[-1], heap[index]
    
    heap.pop()
    # check for leaf
    if index < len(heap):
        _siftup(heap, index)
        _siftdown(heap, 0, index)


def remove_from_heaps(min_heap, max_heap, value):
    if value >= min_heap[0]:
        remove_from_heap(min_heap, value)
    else:
        remove_from_heap(max_heap, -value)


def sliding_median(nums, w):
    min_heap, max_heap = [], []

    for i in range(w):
        update_heaps(min_heap, max_heap, nums[i])

    for i in range(w, len(nums)):
        sys.stdout.write(str(get_median(min_heap, max_heap)) + " ")
        
        update_heaps(min_heap, max_heap, nums[i])
        remove_from_heaps(min_heap, max_heap, nums[i - w])
        
    print(get_median(min_heap, max_heap))


def main():
    n, w = map(int, sys.stdin.readline().split())
    nums = [int(i) for i in sys.stdin.readline().split()]

    sliding_median(nums, w)


if __name__ == "__main__":
    main()
