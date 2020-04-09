# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head and head.next:
            slow, fast = head, head.next

            while slow != fast:                
                if not fast or not fast.next:
                    return False
                
                slow = slow.next
                fast = fast.next.next 
            return True
        return False

    def hasCycle_simple(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:                                
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True
        return False


        