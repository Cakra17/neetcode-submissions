# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue: deque[Optional[ListNode]] = deque()
        res: Optional[ListNode] = None

        for l in lists:
            queue.append(l)

        while queue:
            if not res:
                res = queue.popleft()
            else:
                # combine
                # sort
                head = res
                curr = queue.popleft()
                q = deque()

                while head and curr:
                    if head.val <= curr.val:
                        q.append(head) 
                        head = head.next
                    else:
                        q.append(curr)
                        curr = curr.next 
                
                while head:
                    q.append(head)
                    head = head.next
                
                while curr:
                    q.append(curr)
                    curr = curr.next
                
                curr = res = None
                while q:
                    if not curr:
                        curr = q.popleft()
                        res = curr
                    else:
                        curr.next = q.popleft()
                        curr = curr.next
        return res


