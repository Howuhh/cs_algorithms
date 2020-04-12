# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = merged = ListNode(None)
                
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
                
        curr.next = l1 or l2

        return merged.next

    def mergeTwoLists_rec(self, l1: ListNode, l2: ListNode) -> ListNode:
        # base case: one list is empty
        if not l1 or not l2:
            return l1 or l2

        # merge in order
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists_rec(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_rec(l1, l2.next)
            return l2