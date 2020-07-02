
def n_bit_string(n):
    mod = 10**9 + 7
    # well, thats a python thing, ideally it will overflow, solution:
    # 2**k % mod in loop for k
    return 2**n % mod

def main():
    n = int(input())
    print(n_bit_string(n))


if __name__ == "__main__":
    main()