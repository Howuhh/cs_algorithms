from random import randint


def poly_hash(S, p, a):
    hash_value = 0

    for i in range(len(S)):
        power = len(S) - i - 1
        hash_value += (ord(S[i]) % p) * (a**power % p)

    return hash_value % p


# def search_pattern_test(text, pattern):
#     w = len(pattern)
#     p, a = 1000007, 34

#     hash_values, pattern_hash = [], poly_hash(pattern, p, a)

#     for i in range(0, len(text) - w + 1):
#         hash_values.append((poly_hash(text[i: i + w], p, a), i))

#     print(pattern_hash, hash_values)


def rolling_hash_search(text, pattern):
    "Rabin-Karp Algorithm"
    w = len(pattern)
    p = randint(2*28, 2**36)
    a = randint(1, w)

    hash_values, pattern_hash = [], poly_hash(pattern, p, a)

    # precompute update values
    a_w_p = a**(w - 1) % p
    a_p = a % p

    prev_hash = None
    for i in range(0, len(text) - w + 1):
        if prev_hash:
            new_hash = prev_hash - (ord(text[i - 1]) % p) * a_w_p
            new_hash = new_hash * a_p + (ord(text[i + w - 1]) % p)

            prev_hash = new_hash % p
        else:
            prev_hash = poly_hash(text[i:i + w], p, a)
        hash_values.append((prev_hash, i))

    match_index = []
    for hash_, i in hash_values:
        if hash_ == pattern_hash and text[i: i + w] == pattern:
            match_index.append(i)

    return match_index


def main():
    pattern, text = input(), input()
    print(*rolling_hash_search(text, pattern))


if __name__ == "__main__":
    main()



    