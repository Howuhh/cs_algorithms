# well thats a problem from leetcode


def solve(n, numbers):
    return (n*(n+1) // 2) - sum(numbers)


def main():
    n = int(input())
    seq = [int(i) for i in input().split()]

    print(solve(n, seq))


if __name__ == "__main__":
    main()