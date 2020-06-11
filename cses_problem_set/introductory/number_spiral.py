
def num_spiral(y, x):
    if x > y:
        if x % 2 == 1:
            return x**2 - (y - 1)
        else:
            return (x - 1)**2 + y
    else:
        if y % 2 == 1:
            return (y - 1)**2 + x
        else:
            return y**2 - (x - 1)


def main():
    n = int(input())

    for _ in range(n):
        y, x = map(int, input().split())

        print(num_spiral(y, x))


if __name__ == "__main__":
    main()