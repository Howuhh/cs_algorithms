

def argmax(seq):
    max_idx, max_value = max(enumerate(seq), key=lambda tup: tup[1])
    return max_idx, max_value


def lis_bottom_up(A):
    D = [1] * len(A)

    for i in range(len(A)):
        for j in range(1, i):
            if A[j] <= A[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1

    return max(D)


def count_LIS(seq) -> int:
    lis_counts = [1] * len(seq)

    # count lis
    for i in range(len(seq)):
        for j in range(1, i):
            if seq[j] <= seq[i] and lis_counts[j] + 1 > lis_counts[i]:
                lis_counts[i] += lis_counts[j] + 1

    max_idx, max_lis = argmax(lis_counts)

    return max_idx, max_lis, lis_counts


def get_li_subseq(max_idx, seq, lis_counts):
    subseq = [seq[max_idx]]

    prev_count, prev_idx = lis_counts[max_idx], max_idx
    for i in range(max_idx - 1, -1, -1):
        if (lis_counts[i] == prev_count - 1) and seq[i] <= seq[prev_idx]:
            subseq.append(seq[i])
            prev_count, prev_idx = lis_counts[i], i

    return subseq[::-1]


if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split()))
    print(seq)

    # key = lambda x,y:  (y % x == 0)
    # max_idx, max_lis, lis_counts = count_LIS(seq)
    # subseq = get_li_subseq(max_idx, seq, lis_counts)

    # print(max_lis)
    print(lis_bottom_up(seq))
