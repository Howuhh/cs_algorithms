


def three_sum(nums, target):

    for i, (num, s_i) in enumerate(nums):
        two_target = target - num

        left, right = i + 1, len(nums) - 1
        while left < right:
            
            two_sum = nums[left][0] + nums[right][0]
            
            if two_sum == two_target:
                return [s_i + 1, nums[left][1] + 1, nums[right][1] + 1]
            elif two_sum < two_target:
                left = left + 1
            else:
                right = right - 1
        
    return ["IMPOSSIBLE"]


def main():
    n, target = map(int, input().split())
    nums = [(int(i), idx) for idx, i in enumerate(input().split())]

    print(*three_sum(sorted(nums), target))


if __name__ == "__main__":
    main()