# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1

        curr = head = None
        q = deque()
        while list1 and list2:
            if list1.val <= list2.val:
                q.append(list1.val)
                list1 = list1.next
            else:
                q.append(list2.val)
                list2 = list2.next

        while list1:
            q.append(list1.val)
            list1 = list1.next
        
        while list2:
            q.append(list2.val)
            list2 = list2.next

        while q:
            if not curr:
                n = ListNode(q.popleft(), None)
                curr = head = n
            else:
                n = ListNode(q.popleft(), None)
                curr.next = n
                curr = curr.next
        return head
