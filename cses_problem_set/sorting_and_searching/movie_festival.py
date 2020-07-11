
def max_films(films):
    count = 0 

    prev_end = 0
    for start, end in films:
        if start >= prev_end:
            count += 1
            prev_end = end

    return count


def main():
    films = []

    for _ in range(int(input())):
        a, b = map(int, input().split())
        films.append((a, b))

    films.sort(key=lambda t: t[1])

    print(max_films(films))


if __name__ == "__main__":
    main()