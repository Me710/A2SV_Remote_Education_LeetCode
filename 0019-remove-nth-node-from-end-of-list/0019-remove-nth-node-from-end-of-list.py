# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        left = dummy 
        right = head
        
        # Move right pointer n steps ahead
        for i in range(n):
            right = right.next
            
        # Move pointers together until right hits end
        while right:
            left = left.next
            right = right.next
            
        # Delete node
        left.next = left.next.next
        
        return dummy.next