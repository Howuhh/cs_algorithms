# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr, prev = head, None
        
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            
        return prev