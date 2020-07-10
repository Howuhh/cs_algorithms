import sys
import time

from collections import OrderedDict

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

    result = give_tickets(sorted(prices), max_prices)

    for t in result:
        sys.stdout.write(str(t) + "\n")


if __name__ == "__main__":
    main()