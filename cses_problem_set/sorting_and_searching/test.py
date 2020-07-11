import sys
import bisect

input = sys.stdin.readline
writer = sys.stdout.write
upper_bound = bisect.bisect_right


def main():
    n,m = map(int,input().split())
    
    H = [int(x) for x in input().split()]
    H.sort()
 
    P = list(range(n+1))

    for t in sys.stdin.read().split():
        old_a = a = upper_bound(H, int(t))
        
        while a != P[a]:
            a = P[a]

        while old_a != a:
            P[old_a], old_a = a, P[old_a]
        
        if a:
            writer(str(H[a-1]))
            writer('\n')
            P[a] = a-1
        else:
            writer('-1\n')

if __name__ == "__main__":
    main()