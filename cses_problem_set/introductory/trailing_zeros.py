

def num_zeros(n):
    # count number of 5's 
    count = 0

    for i in range(1, n + 1):
        num_of_fives = n // 5**i
        if num_of_fives == 0:
            break
        count += num_of_fives

    return count


def main():
    n = int(input())

    print(num_zeros(n))


if __name__ == "__main__":
    main()