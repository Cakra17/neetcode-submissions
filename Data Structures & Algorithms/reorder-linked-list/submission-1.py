# Definition for singly-linked list.
# class ListNode:
from types import coroutine
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, next = None, head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        # split into 2 list
        f = s = head
        prev = None
        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next
        
        h1 = head
        h2 = prev.next
        prev.next = None
        
        # reverse the second
        h2 = self.reverse(h2)
        
        # merge
        q = deque()
        while h1 and h2:
            q.append(h1)
            q.append(h2)
            h1 = h1.next
            h2 = h2.next

        while h1:
            q.append(h1)
            h1 = h1.next

        while h2:
            q.append(h2)
            h2 = h2.next

        res = merged = None
        while q:
            if not res:
                res = q.popleft()
            else:
                res.next = q.popleft()
                res = res.next

        head = res

        

