# https://cp-algorithms.com/algebra/extended-euclid-algorithm.html
def gcd(a, b, x=None, y=None):
    if b == 0:
        return (a, 1, 0)

    g, x_prev, y_prev = gcd(b, a % b, x, y)

    x = y_prev
    y = x_prev - y_prev * (a // b)

    return g, x, y


def solve_linear(a, b, c):
    "solve Ax + By = C"
    g, x_p, y_p = gcd(a, b)

    if c % g != 0:
        return False

    x = x_p * (c // g)
    y = y_p * (c // g)
    return x, y  # one solution


def main():
    a, b = 234, 24
    print(gcd(a, b))


if __name__ == "__main__":
    main()