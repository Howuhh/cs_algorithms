from collections import deque

# TODO: not solved, approach with heaps (??)
def partition(nums, l, r):
    x, j = nums[l], l

    for i in range(l + 1, r + 1):
        if nums[i] < x:
            j = j + 1
            nums[j], nums[i] = nums[j], nums[i]

    nums[l], nums[j] = nums[j], nums[l] 
    return j


def quick_select(nums, k):
    left, right = 0, len(nums) - 1

    while left <= right:
        pivot = partition(nums, left, right)

        if pivot == len(nums) - k:
            return nums[pivot]
        elif pivot < len(nums) - k:
            left = pivot + 1
        else:
            right = pivot - 1


def median(nums):
    if len(nums) % 2 != 0:
        return quick_select(nums, (len(nums) // 2) + 1)
    else:
        return min(
            quick_select(nums, (len(nums) // 2) + 1),
            quick_select(nums, (len(nums) // 2) - 1 + 1)
            )


def sliding_median(nums, w):
    # n - k + 1
    queue = deque(sorted(nums[:w]))

    for i in range(w, len(nums)):
        window = queue.copy()
        
        print(median(window), end=" ")
        
        queue.popleft()
        queue.append(nums[i])

    window = queue.copy()
    print(median(window))


def main():
    n, w = map(int, input().split())
    nums = [int(i) for i in input().split()]

    # print(nums)
    sliding_median(nums, w)


def test():
    nums = [5, 4, 2, 3, 1, 6]

    print(median(nums))


if __name__ == "__main__":
    main()