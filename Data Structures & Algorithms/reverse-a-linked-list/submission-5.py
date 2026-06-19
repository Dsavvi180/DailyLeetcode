# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        node = head.next
        prevNode = head
        prevNode.next = None
        while node and node.next:
            nextNode = node.next
            node.next = prevNode
            prevNode = node
            node = nextNode
        node.next = prevNode
        return node 
        