
def weird_algo(n):
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
    print(*weird_algo(n))


if __name__ == "__main__":
    main()