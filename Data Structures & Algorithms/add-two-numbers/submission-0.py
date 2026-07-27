# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        ans = res = None

        while l1 and l2:
            sm = l1.val + l2.val + carry
            rm = sm % 10
            carry = sm // 10

            nd = ListNode(rm, None)

            if not res:
                res = nd
                ans = res
            else:
                res.next = nd
                res = res.next

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sm = l1.val + carry
            rm = sm % 10
            carry = sm // 10

            nd = ListNode(rm, None)

            if not res:
                res = nd
            else:
                res.next = nd 
                res = res.next
            
            l1 = l1.next

        while l2:
            sm = l2.val + carry
            rm = sm % 10
            carry = sm // 10

            nd = ListNode(rm, None)

            if not res:
                res = nd
            else:
                res.next = nd
                res = res.next
            
            l2 = l2.next

        if carry > 0:
            nd = ListNode(carry, None)
            res.next = nd
            res = res.next

        return ans