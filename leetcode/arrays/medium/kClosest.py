import heapq
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = []
        
        for i, (x, y) in enumerate(points):
            dist.append([sqrt(x**2 + y**2), i])
            
        dist.sort()
        k_smallest_idx = self.findKSmallest(dist, K)
        
        return [points[idx[1]] for idx in k_smallest_idx]
        
    def findKSmallest(self, nums, k):  # O(n + k*logn)
        heap = nums
        heapq.heapify(heap)
        
        closest = []
        for _ in range(k):
            closest.append(heapq.heappop(heap))
            
        return closest
    