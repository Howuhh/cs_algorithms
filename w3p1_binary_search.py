

def binary_search(arr, item, l, r):
    if l > r or l >= len(arr):
        return -1
    
    mid = (l + r) // 2
    if arr[mid] == item:
        return mid
    elif arr[mid] < item:
        idx = binary_search(arr, item, mid + 1, r)
    else:
        idx = binary_search(arr, item, l, mid - 1)

    return idx


def binary_search_loop(arr, item):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] == item:
            return mid + 1
        elif arr[mid] < item:
            left = mid + 1
        else:
            right = mid

    return -1


def main():
    n, *data = map(int, input().split())
    k, *search = map(int, input().split())
    print(*[binary_search_loop(data, item) for item in search])

if __name__ == "__main__":
    main() 