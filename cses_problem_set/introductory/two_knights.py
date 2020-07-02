
def num_knights(k):
    kk = k**2
    # how many 2x3 and 3x2 in kxk table?
    return kk*(kk - 1)//2 - 4*(k - 2)*(k - 1)


def main():
    n = int(input())

    for k in range(1, n + 1):
        print(num_knights(k))


if __name__ == "__main__":
    main()