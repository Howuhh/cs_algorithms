


# n is only <= 20
def min_div_exp(array):
    min_div, n = float("inf"), len(array)

    for i in range(2**n, 2**(n + 1)):
        mask = bin(i)[3:]

        left, right = 0, 0
        for j, m in enumerate(mask):
            if m == "1":
                left += array[j]
            else:
                right += array[j]

        min_div = min(min_div, abs(left - right))

    return min_div


def min_div_rec(array):
    total = sum(array)

    def _div(index, subsum):
        if index == len(array):
            return abs(subsum - (total - subsum))

        return min(
            _div(index + 1, subsum), 
            _div(index + 1, subsum + array[index])
            )

    return _div(0, 0)


def main():
    n = int(input())
    apples = [int(a) for a in input().split()]

    # print(min_div(apples))
    # print(min_div_exp(apples))
    print(min_div_rec(apples))


if __name__ == "__main__":
    main()