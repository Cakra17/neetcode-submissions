"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mapFromOldToNew = {}
        curr = head

        while curr:
            n = Node(curr.val)
            mapFromOldToNew[curr] = n
            curr = curr.next
        
        curr = head
        while curr:
            n = mapFromOldToNew[curr]
            n.next = mapFromOldToNew[curr.next] if curr.next else None
            n.random = mapFromOldToNew[curr.random] if curr.random else None
            curr = curr.next
        
        return mapFromOldToNew[head]

