# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        ln = 0

        curr = head
        while curr:
            ln += 1
            curr = curr.next
        
        curr = head
        while curr:
            if ln == n:
                if not prev:
                    curr = curr.next
                else:
                    prev.next = curr.next
                break
            prev = curr
            ln -= 1
            curr = curr.next
        return head if prev else curr
        