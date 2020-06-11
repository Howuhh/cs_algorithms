
def num_turns(nums):
    count = 0

    prev = 0
    for i in range(1, len(nums)):
        if nums[i] < (nums[i - 1] + prev):
            diff = nums[i - 1] + prev - nums[i]

            count += diff
            prev = diff
        else:
            prev = 0

    return count


def main():
    n = int(input())
    nums = [int(i) for i in input().split()]

    print(num_turns(nums))


if __name__ == "__main__":
    main()