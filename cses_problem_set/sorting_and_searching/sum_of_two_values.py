

def target_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        two_sum = nums[left][0] + nums[right][0]

        if two_sum == target:
            return nums[left][1] + 1, nums[right][1] + 1
        elif two_sum < target:
            left = left + 1
        else:
            right = right - 1

    return None


def main():
    n, target = map(int, input().split())
    nums = [(int(i), idx) for idx, i in enumerate(input().split())]
    nums.sort()

    res = target_sum(nums, target)
    if res:
        print(*res)
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    main()