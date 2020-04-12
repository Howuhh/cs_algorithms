from math import inf


class Solution:
    def climbStairs_rec(self, n: int) -> int:
        D = [inf] * (n + 1)
        
        def distinct(D, n):
            if D[n] == inf:
                if n == 0 or n == 1:
                    D[n] = 1
                else:
                    D[n] = distinct(D, n - 1) + distinct(D, n - 2)
                
            return D[n]

        return distinct(D, n)

    def climbStairs_iter(self, n: int) -> int:
        D = [1, 1] + [0] * (n - 1)

        for i in range(2, n + 1):
            D[i] = D[i - 1] + D[i - 2]

        return D[n]

    def climbStairs_fib(self, n: int) -> int:
        d1, d2 = 1, 1

        for i in range(2, n + 1):
            d1, d2 = d2, d1 + d2

        return d2