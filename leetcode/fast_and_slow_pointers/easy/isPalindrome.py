# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 1 -> 2 -> 2 -> 1
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head:
            slow, fast = head, head

            # find middle
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            # reverse after middle
            prev, curr = None, slow

            while curr:
                curr.next, prev, curr = prev, curr, curr.next

            # check for palindrome
            start, mid = head, prev
            if start.val != mid.val:
                return False

            while mid:
                if start.val != mid.val:
                    return False

                start = start.next
                mid = mid.next
        return True