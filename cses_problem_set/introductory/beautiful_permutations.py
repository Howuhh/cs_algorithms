
# def permute(n):
#     cands = range(1, n + 1)

#     perms = []
#     def _permute(perm, chosen):
#         if len(perm) == len(cands):
#             perms.append(perm)
#             return True

#         for i, num in enumerate(cands):
#             if chosen[i]:
#                 continue
            
#             if perm and abs(num - perm[-1]) == 1:
#                 continue

#             chosen[i] = True
#             find = _permute(perm + [num], chosen)
#             if find:
#                 break
#             chosen[i] = False

#     _permute([], [False] * n)

#     return perms

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