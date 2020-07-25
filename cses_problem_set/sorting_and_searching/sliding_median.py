from collections import deque
from heapq import heappop, heappush


# def update_heaps(min_heap, max_heap, value):
#     # push
#     if len(min_heap) == 0 or value < min_heap[-1]:
#         heappush(min_heap, value)
#     else:
#         heappush(max_heap, -1 * value)

#     # rebalance
#     if len(min_heap) - len(max_heap) > 1:
#         heappush(max_heap, -1 * heappop(min_heap))
#     else:
#         heappush(min_heap, -1 * heappop(max_heap))


# def get_median(min_heap, max_heap):
#     if len(min_heap) == len(max_heap):
#         return min_heap[-1]
#     else:
#         return max_heap[-1]


# def sliding_median(nums, w_size):
#     medians = []

#     min_heap = []  # for max values
#     max_heap = []  # for min values

#     for i in range(nums):
        





def main():
    n, w = map(int, input().split())
    nums = [int(i) for i in input().split()]

    # print(nums)
    sliding_median(nums, w)




if __name__ == "__main__":
    main()



# # TODO: not solved, approach with heaps (??)
# def partition(nums, l, r):
#     x, j = nums[l], l

#     for i in range(l + 1, r + 1):
#         if nums[i] < x:
#             j = j + 1
#             nums[j], nums[i] = nums[j], nums[i]

#     nums[l], nums[j] = nums[j], nums[l] 
#     return j


# def quick_select(nums, k):
#     left, right = 0, len(nums) - 1

#     while left <= right:
#         pivot = partition(nums, left, right)

#         if pivot == len(nums) - k:
#             return nums[pivot]
#         elif pivot < len(nums) - k:
#             left = pivot + 1
#         else:
#             right = pivot - 1


# def median(nums):
#     if len(nums) % 2 != 0:
#         return quick_select(nums, (len(nums) // 2) + 1)
#     else:
#         return min(
#             quick_select(nums, (len(nums) // 2) + 1),
#             quick_select(nums, (len(nums) // 2) - 1 + 1)
#             )


# def sliding_median(nums, w):
#     # n - k + 1
#     queue = deque(sorted(nums[:w]))

#     for i in range(w, len(nums)):
#         window = queue.copy()
        
#         print(median(window), end=" ")
        
#         queue.popleft()
#         queue.append(nums[i])

#     window = queue.copy()
#     print(median(window))
