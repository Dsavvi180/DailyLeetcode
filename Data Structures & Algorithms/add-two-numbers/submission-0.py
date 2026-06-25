# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        headL1 = l1
        while headL1.next:
            tmpVal = str(headL1.next.val)+str(headL1.val)
            headL1 = headL1.next
            headL1.val = tmpVal

        headL2 = l2
        while headL2.next:
            tmpVal = str(headL2.next.val)+str(headL2.val)
            headL2 = headL2.next
            headL2.val = tmpVal
        
        sumVal = str(int(headL2.val)+ int(headL1.val))
        lenSumStr = len(sumVal)-1

        newList = l1
        while newList.next and lenSumStr>=0:
            newList.val = int(sumVal[lenSumStr])
            newList = newList.next 
            lenSumStr -=1
        newList.val = int(sumVal[lenSumStr])
        lenSumStr -= 1

        if lenSumStr>=0 and not newList.next:
            while lenSumStr>=0:
                newList.next = ListNode(sumVal[lenSumStr])
                newList = newList.next
                lenSumStr -= 1
            
        elif lenSumStr==0 and newList.next:
            newList.next = None
        return l1


        



