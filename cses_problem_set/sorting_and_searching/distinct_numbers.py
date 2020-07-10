
def n_distinct(arr):
    dist, count = set(), 0

    for num in arr:
        if num not in dist:
            dist.add(num)
            count += 1

    # len(set(arr))
    return count


def main():
    n = input()
    array = [int(i) for i in input().split()]

    print(n_distinct(array))

if __name__ == "__main__":
    main()