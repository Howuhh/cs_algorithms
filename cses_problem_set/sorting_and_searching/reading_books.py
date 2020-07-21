
def min_time(books):
    return max(sum(books), 2*books[-1])


def main():
    n = input()
    books = [int(i) for i in input().split()]

    print(min_time(sorted(books)))

if __name__ == "__main__":
    main()