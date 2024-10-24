# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow = fast = head 
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr

        right = prev
        left = head
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
