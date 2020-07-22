
def subarray_sums(nums, target):  # O(n^2)
    cum_sum = [0] * (len(nums) + 1)
    
    for i in range(1, len(nums) + 1):
        cum_sum[i] = nums[i - 1] + cum_sum[i - 1] 

    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if cum_sum[j] - cum_sum[i] == target:
                count += 1
            
    return count


# for negative values also 
def subarray_sums_map(nums, target):
    sum_freq = {0: 1}

    acc, count = 0, 0
    for i in range(len(nums)):
        acc += nums[i]

        # sum[i:j] = sum[0:j] - sum[0:i] = k
        # sum[0:i] = sum[0:j] - k <- count such arrays
        if acc - target in sum_freq:
            count += sum_freq[acc - target]

        sum_freq[acc] = sum_freq.get(acc, 0) + 1

    return count


# only for positive numbers
def subarray_sums_pointers(nums, target):
    j, acc, count = 0, 0, 0

    for i in range(len(nums)):
        acc += nums[i]

        if acc == target:
            count += 1

        while acc > target and j < i:
            acc -= nums[j]
            if acc == target:
                count += 1
            j += 1

    return count


def main():
    n, target = map(int, input().split())
    nums = [int(i) for i in input().split()]

    print(subarray_sums_pointers(nums, target))


if __name__ == "__main__":
    main()