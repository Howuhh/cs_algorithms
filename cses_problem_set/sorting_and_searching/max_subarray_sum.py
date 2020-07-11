
def max_subarr(nums):
    dp = [0] * len(nums)

    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])

    return max(dp)


def main():
    n = int(input())
    nums = [int(i) for i in input().split()]

    print(max_subarr(nums))


if __name__ == "__main__":
    main()