

def subarray_div(nums, target):
    mod_freq = {}

    # sum(i, j) = sum(j) - sum(i - 1) ->
    # sum(i, j) = q1 * n + r1 - (q2 * n + r1) ->
    # sum(i, j) = (q1 - q2)*n + (r1 - r2) ->
    # if n | sum(i, j), then (r1 - r2) | n and r1 == r2
    # then sum(i) = sum(j) (mod n)
    
    acc, count = 0, 0
    for i in range(len(nums)):
        acc += nums[i]

        mod = acc % target
        mod_freq[mod] = mod_freq.get(mod, 0) + 1 # count rems

    for mod, freq in mod_freq.items():
        if freq > 1:
            # n(n - 1) / 2 ways to chose 2 arrays from n
            count += (freq * (freq - 1)) // 2 
    
    # count all single arrays
    count += mod_freq.get(0, 0)

    return count


def main():
    n = int(input())
    nums = [int(i) for i in input().split()]

    # print(subarray_div(nums, n))
    print(subarray_div_ex(nums, n))


if __name__ == "__main__":
    main()