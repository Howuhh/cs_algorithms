

# likely will not work, so what about heaps? - not work!
def max_films(times, k):
    count = 0
    attend = k

    for time in times:
        if time[1] and attend:
            attend = attend - 1
            count = count + 1
        elif not time[1]:
            if attend < k:
                attend = attend + 1

    return count


def main():
    n, k = map(int, input().split())
    times = []

    for _ in range(n):
        s, e = map(int, input().split())
        times.append((s, True))
        times.append((e, False))

    times.sort()

    print(max_films(times, k))


if __name__ == "__main__":
    main()