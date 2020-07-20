import sys
from time import time
from bisect import bisect_right

def bisect_left(nums, value):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2 

        if nums[mid] == value:
            return mid
        elif nums[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left - 1


# TIME LIMIT: would work in cpp
def give_tickets(prices, max_prices):  # O(n^2)
    result = []

    for max_ in max_prices:
        idx = bisect_left(prices, max_)
        
        if -1 < idx < len(prices):
            result.append(prices[idx])
            del prices[idx]  # O(n) - need some how delete picked item from an array
        else:
            result.append(-1)

    return result


def main():
    n, m = map(int, input().split())

    prices = [int(i) for i in sys.stdin.readline().split()]
    max_prices = [int(i) for i in sys.stdin.readline().split()]

    s1 = time()
    result = give_tickets(sorted(prices), max_prices)
    print(time() - s1)

    s2 = time()
    result_r = give_tickets_right(sorted(prices), max_prices)
    print(time() - s2)

    print(result == result_r)

    # for t in result:
        # sys.stdout.write(str(t) + "\n")


if __name__ == "__main__":
    main()

# TODO: solution from site 
# import sys
# import bisect

# input = sys.stdin.readline
# writer = sys.stdout.write
# upper_bound = bisect.bisect_right

# # TODO: how it works???
# def main():
#     n,m = map(int,input().split())
    
#     H = [int(x) for x in input().split()]
#     H.sort()
 
#     P = list(range(n+1))

#     for t in sys.stdin.read().split():
#         old_a = a = upper_bound(H, int(t))
        
#         while a != P[a]:
#             a = P[a]

#         while old_a != a:
#             P[old_a], old_a = a, P[old_a]
        
#         if a:
#             writer(str(H[a-1]))
#             writer('\n')
#             P[a] = a-1
#         else:
#             writer('-1\n')

# if __name__ == "__main__":
#     main()