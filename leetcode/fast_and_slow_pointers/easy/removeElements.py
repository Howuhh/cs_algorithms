# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head:
            node = head
            # 1 -> 2 -> 2 -> 1 == 1 -> 1
            while node and node.next:   
                if node.next.val == val:
                    node.next = node.next.next
                else:
                    node = node.next
                    
            if head and head.val == val:
                head = head.next
        return head
