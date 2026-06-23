# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next

        listOfNodes = [head]
        tmp = head.next

        while tmp:
            listOfNodes.append(tmp)
            tmp = tmp.next

        nthFromEnd = len(listOfNodes)-n
        print(nthFromEnd)
        if nthFromEnd==0:
            return head.next
        prev = listOfNodes[nthFromEnd-1]
        if nthFromEnd +1> len(listOfNodes)-1:
            prev.next = None
        else:
            nxt = listOfNodes[nthFromEnd+1]
            prev.next = nxt
        return head
        