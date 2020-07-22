

def subarray_div(nums, target):
    mod_freq = {}

    acc, count = 0, 0
    for i in range(len(nums)):
        acc += nums[i]

        mod = acc % target
        mod_freq[mod] = mod_freq.get(mod, 0) + 1

    for mod, freq in mod_freq.items():
        if freq > 1:
            count += (freq * (freq - 1)) // 2
    
    count += mod_freq.get(0, 0)

    return count


def main():
    n = int(input())
    nums = [int(i) for i in input().split()]

    print(subarray_div(nums, n))


if __name__ == "__main__":
    main()