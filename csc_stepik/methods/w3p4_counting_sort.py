
def counting_sort(arr, max_bound=11):
    counts = [0] * max_bound
    sorted_arr = [0] * len(arr)

    # freq count
    for el in arr:
        counts[el] += 1

    # cumulative sum
    for i in range(1, len(counts)):
        counts[i] = (counts[i] + counts[i - 1]) 

    for el in arr:
        sorted_arr[counts[el] - 1] = el
        counts[el] -= 1

    return sorted_arr


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    sorted_arr = counting_sort(arr)

    print(*sorted_arr)

if __name__ == "__main__":
    main()

