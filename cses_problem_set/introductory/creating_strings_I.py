
def permute_string(string):
    perms = set()

    def _perm(perm, chosen):
        if len(perm) == len(string):
            perms.add(perm)
            return

        for i, char in enumerate(string):
            if chosen[i]:
                continue

            chosen[i] = True
            _perm(perm + char, chosen)
            chosen[i] = False
    _perm("", [False] * len(string))

    return perms


def main():
    string = input()
    perms = sorted(permute_string(string))

    print(len(perms))
    for perm in perms:
        print(perm)

if __name__ == "__main__":
    main()