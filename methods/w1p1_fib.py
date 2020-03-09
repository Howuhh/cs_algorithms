# Дано целое число 1 ≤ n ≤ 40 , необходимо вычислить n-е число Фибоначчи 
# (напомним, что F_0 = 0, F_1 = 1 F_n=F_{n-1}+F_{n-2} при n ≥2).


def fib_rec(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_table(n: int) -> int:
    assert n > 0, "n >= 1"

    table = [0]*(n+1)
    table[0] = 0
    table[1] = 1

    for i in range(2, n+1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


def fib_vars(n: int) -> int:
    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


def fib_last_digit(n: int) -> int:
    "f_i mod 10 + f_i+1 mod 10 = F_i+2 mod 10"
    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, (a + b) % 10

    return b


# найти остаток от деления n числа фиб на m
def fib_mod(n: int, m: int) -> int:
    rem = [0, 1]

    for i in range(2, n + 1):
        rem.append((rem[i - 1] + rem[i - 2]) % m)

        if rem[i - 1] == 0 and rem[i] == 1:
            return rem[n % (len(rem) - 2)]

    return rem.pop()


if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    # n, m = 10**12, 10**3
    
    # print(fib_vars(n))
    print(fib_mod(n, m))
    