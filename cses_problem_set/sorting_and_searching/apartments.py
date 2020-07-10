from math import inf


def max_applicants(room_sizes, desired, max_diff): # O(n)
    i, j, count = 0, 0, 0

    while i < len(room_sizes) and j < len(desired):
        if abs(room_sizes[i] - desired[j]) <= max_diff:
            count += 1
            i += 1
            j += 1
        elif room_sizes[i] > desired[j]:
            j += 1
        else:
            i += 1
    return count


def max_applicants_naive(sizes, desired, diff): # simple O(n^2)
    count = 0

    for app in desired:
        for i, size in enumerate(sizes):
            if abs(app - size) <= diff:
                sizes[i] = inf

                count += 1
                break

    return count


def main():
    n, m, k = map(int, input().split())
    desired = [int(i) for i in input().split()]
    sizes = [int(i) for i in input().split()]

    print(max_applicants(sorted(sizes), sorted(desired), k))


if __name__ == "__main__":
    main()