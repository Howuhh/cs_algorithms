import heapq

from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        
        for word in words:
            freq[word] = freq.get(word, 0) + 1
            
        heap = [(-count, word) for word, count in freq.items()]
        heapq.heapify(heap)
        
        top_k_freq = []
        for _ in range(k):  # O(n + klogn)
            top_k_freq.append(heapq.heappop(heap))
            
        return [word[1] for word in sorted(top_k_freq)]  # O(klogk)