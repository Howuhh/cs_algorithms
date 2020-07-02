

def permute(n):
    if 1 < n <= 3:
        return None
    
    perm = []
    for i in range(2, n + 1, 2):
        perm.append(i)

    for i in range(1, n + 1, 2):
        perm.append(i)

    return perm

def main():
    n = int(input())

    perm = permute(n)
    if perm:
        print(*perm)
    else:
        print("NO SOLUTION")


if __name__ == "__main__":
    main()