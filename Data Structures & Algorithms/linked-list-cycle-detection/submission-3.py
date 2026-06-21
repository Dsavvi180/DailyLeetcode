# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        nodeIds = set([id(head)])

        while head:
            if not head.next:
                return False
            if id(head.next) in nodeIds:
                return True
            else:
                nodeIds.add(id(head.next))
            head = head.next
        