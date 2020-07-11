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


def give_tickets_right(prices, max_prices):  # O(n^2)
    sold = [False] * len(prices)
    result = []

    for max_ in max_prices:
        idx = bisect_right(prices, max_)

        if idx >= len(prices) or prices[idx] != max_:
            idx = idx - 1

        while idx > -1 and sold[idx]:
            idx = idx - 1

        if idx > -1:
            result.append(prices[idx])
            sold[idx] = True
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