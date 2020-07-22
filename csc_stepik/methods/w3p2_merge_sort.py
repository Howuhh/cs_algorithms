from collections import deque
import sys

# time limit??
def merge_q(arr1, arr2):
    tmp = []
    count = 0

    while arr1 and arr2:
        if arr1[0] <= arr2[0]:
            tmp.append(arr1.popleft())
        else:
            tmp.append(arr2.popleft())
            count += len(arr1)

    tmp.extend(arr1 or arr2)

    return tmp, count


def merge(arr1, arr2, count=False):
    new = []
    inverse = 0

    i, j = 0, 0
    len1, len2 = len(arr1), len(arr2)
    while i < len1 and j < len2:
        if arr1[i] <= arr2[j]:
            new.append(arr1[i])
            
            i += 1
        else:
            new.append(arr2[j])

            inverse += (len1 - i)
            j += 1

    if i < len1:
        [new.append(arr1[k]) for k in range(i, len1)]

    if j < len(arr2):
        [new.append(arr2[k]) for k in range(j, len2)]

    if count:
        return new, inverse
    return new


def merge_sort_rec(arr, l, r):
    if l < r:
        mid = (l + r) // 2

        left, lcount = merge_sort_rec(arr, l, mid)
        right, rcount = merge_sort_rec(arr, mid + 1, r)
        merged, count = merge(left, right, True)

        return (merged, lcount + count + rcount)
    else:
        return ([arr[l]], 0)


def merge_sort(arr):
    queue = deque()
    [queue.appendleft([el]) for el in arr]

    while len(queue) > 1:
        merged, i_count = merge(queue.pop(), queue.pop())
        queue.appendleft(merged)

    return queue.pop()


def naive_invers(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j] and i <= j:
                count += 1

    return count


def main():
    n, *test = map(float, sys.stdin.read().split())

    print(merge_sort_rec(deque(test), 0, len(test) - 1)[1])


if __name__ == "__main__":
    main()






# import sys
# from collections import deque

# def merge(arr1, arr2):
#     tmp = deque()
#     count = 0

#     while arr1 and arr2:
#         if arr1[0] <= arr2[0]:
#             tmp.append(arr1.popleft())
#         else:
#             tmp.append(arr2.popleft())
#             count += len(arr1)

#     tmp.extend(arr1 or arr2)

#     return tmp, count


# def merge_sort(arr, l, r):
#     if l < r:
#         mid = (l + r) // 2

#         left, lcount = merge_sort(arr, l, mid)
#         right, rcount = merge_sort(arr, mid + 1, r)
        
#         merged, count = merge(left, right)
#         return (merged, lcount + count + rcount)
#     else:
#         return (deque(arr[l]), 0)

    
# def main():
#     n, *test = map(float, sys.stdin.read().split())

#     print(merge_sort(deque(test), 0, len(test) - 1)[1])