
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # start from every possible palindrome
        # mid and expand while chars are equal
        max_len, max_pal = 0, ""

        # mid for odd pal (mid)
        for mid in range(len(s)):
            x = 0
            while (mid + x < len(s) and mid - x >= 0) and s[mid - x] == s[mid + x]:
                if 2*x + 1 > max_len:
                    max_len = 2*x + 1
                    max_pal = s[mid - x:mid + x + 1]

                x += 1
                
        # mid for even pal (mid, mid + 1)
        for mid in range(len(s) - 1):
            x = 0
            
            while (mid + 1 + x < len(s) and mid - x >= 0) and s[mid - x] == s[mid + 1 + x]:
                if 2*x + 2 > max_len:
                    max_len = 2*x + 2
                    max_pal = s[mid-x:mid + x + 2]
                x += 1
        
        return max_pal