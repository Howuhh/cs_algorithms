from typing import List
from math import inf


class Solution:
    def maxProfit_naive(self, prices: List[int]) -> int:
        D = [0] * len(prices)
        
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i and prices[j] > prices[i] and prices[j] - prices[i] >= D[i]:
                    D[i] = prices[j] - prices[i]
                    
        return max(D or [0])
    
    def maxProfit_dp(self, prices: List[int]) -> int:
        if not prices:
            return 0

        D, min_price = [0] * len(prices),  prices[0]

        for n in range(1, len(prices)):
            max_n = 0 if min_price > prices[n] else prices[n] - min_price

            D[n] = max(D[n - 1], max_n)
            
            if prices[n] < min_price:
                min_price = prices[n]
        
        return D[-1]
        
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = inf, 0
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
                    