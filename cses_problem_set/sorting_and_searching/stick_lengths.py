

def min_cost(lenghts):
    mid = len(lenghts) // 2

    cost = 0
    for l in lenghts:
        cost += abs(l - lenghts[mid])

    return cost


def main():
    n = input()
    lenghts = [int(i) for i in input().split()]
    lenghts.sort()

    print(min_cost(lenghts))


if __name__ == "__main__":
    main()