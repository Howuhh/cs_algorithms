
def num_knights(k):
    total = k**2
    
    corner = 4 * (total - 4)
    border = (k - 2) * 4 * (total - 6)
    center = (k - 2)** 2 * (total - 9)
    return (corner + border + center) // 2


def main():
    n = int(input())

    for k in range(1, n + 1):
        print(k, num_knights(k))


if __name__ == "__main__":
    main()