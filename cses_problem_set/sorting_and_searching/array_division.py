
def div_possible(nums, mid, k):
    acc, count = 0, 1
    
    for num in nums: 
        acc += num
        
        if acc > mid:
            count += 1
            acc = num
    
    if count > k:
        return False
    return True


def min_k_subdiv(nums, k):
    ans = None

    left, right = max(nums), sum(nums)
    while left <= right:
        mid = (left + right) // 2
            
        if not div_possible(nums, mid, k):
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
            
    return ans


def main():
    n, k = map(int, input().split())
    nums = [int(i) for i in input().split()]
    
    print(min_k_subdiv(nums, k))


if __name__ == "__main__":
    main()