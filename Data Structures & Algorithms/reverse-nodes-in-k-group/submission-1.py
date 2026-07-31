# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        num_of_group = []
        curr = head
        i = 0
        q = deque()

        while curr:
            q.append(curr)
            i += 1
            if i == k or not curr.next:
                num_of_group.append(q)
                q = deepcopy(q)
                q.clear()
                i = 0
            curr = curr.next
        
        res = newHead = None
        for queue in num_of_group:
            isReversed = len(queue) >= k
            if isReversed:
                while queue:
                    if not res:
                        res = queue.pop()
                        newHead = res
                    else:
                        node = queue.pop()
                        res.next = node
                        res = res.next 
                        res.next = None
            else:
                while queue:
                    node = queue.popleft()
                    res.next = node
                    res = res.next
                    res.next = None 

        return newHead