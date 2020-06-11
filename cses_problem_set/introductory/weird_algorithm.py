
def solve(n):
    seq = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n*3 + 1
        seq.append(n)
    return seq


def main():
    n = int(input())
    print(*solve(n))


if __name__ == "__main__":
    main()