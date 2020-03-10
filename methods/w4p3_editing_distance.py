from math import inf

def print_array(array):
    for row in array:
        print(row)


def diff(A, B):
    return 1 if A != B else 0


# https://en.wikipedia.org/wiki/Levenshtein_distance
def levenshtein_dist(seq1, seq2, return_d=False):
    n, m = len(seq1) + 1, len(seq2) + 1
    D = [[0] * m for _ in range(n)]

    # rows
    for i in range(n):
        D[i][0] = i
    
    # cols
    for j in range(m):
        D[0][j] = j

    # D 
    for i in range(1, n):
        for j in range(1, m):
            cost = diff(seq1[i - 1], seq2[j - 1])  # edit cost (zero based -> i - 1)    
            D[i][j] = min(
                D[i][j - 1] + 1,  # insert
                D[i - 1][j] + 1,  # del
                D[i - 1][j - 1] + cost  # edit
            )

    if return_d:
        return D[n - 1][m - 1], D

    return D[n - 1][m - 1]


def levenshtein_dist_rec(seq1, seq2, i=None, j=None):
    n, m = len(seq1) + 1, len(seq2) + 1
    D = [[inf] * m for _ in range(n)]

    if i is None:
        i, j = n - 1, m - 1

    if D[i][j] == inf:
        if i == 0:
            D[i][j] = j
        elif j == 0:
            D[i][j] = i
        else:
            ins = levenshtein_dist_rec(seq1, seq2, i, j - 1) + 1
            del_ = levenshtein_dist_rec(seq1, seq2, i - 1, j) + 1
            edit = levenshtein_dist_rec(seq1, seq2, i - 1, j - 1) + diff(seq1[i - 1], seq2[j - 1])

            D[i][j] = min(ins, del_, edit)

    return D[i][j]


def backtrack_edit(D, seq1, seq2):
    n, m = len(D) - 1, len(D[0]) - 1
    seq1_align = []
    seq2_align = []

    i, j = n, m
    while i > 0 or j > 0:
        if D[i][j] == D[i - 1][j] + 1:
            seq1_align.append(seq1[i - 1])
            seq2_align.append("-")

            i = i - 1
        elif D[i][j] == D[i][j - 1] + 1:
            seq1_align.append("-")
            seq2_align.append(seq2[j - 1])

            j = j - 1
        else:
            seq1_align.append(seq1[i - 1])
            seq2_align.append(seq2[j - 1])

            i, j = i - 1, j - 1

    return "".join(reversed(seq1_align)), "".join(reversed(seq2_align))


def main():
    seq1, seq2 = input(), input()

    dist, D = levenshtein_dist(seq1, seq2, True)
    ans1, ans2 = backtrack_edit(D, seq1, seq2) 
    
    print(ans1)
    print(ans2)


if __name__ == "__main__":
    main() 