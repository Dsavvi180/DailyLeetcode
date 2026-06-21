# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next:
    
            l1 = head
            l2 = head.next
            
            while l2 and l2.next:
                l1 = l1.next
                if l2.next.next:
                    l2 = l2.next.next
                else:
                    l2 = l2.next
            
            l2 = l1.next
            l1.next = None
            # reverse l2:
            currentNode = l2
            nextNode = l2.next
            currentNode.next = None
            while nextNode:
                tmp = currentNode
                currentNode = nextNode
                nextNode = nextNode.next
                currentNode.next = tmp
            
            l2 = currentNode
            l1 = head
            head = None
            newList = ListNode()
            nextNode = newList
            l1Chosen = False
            while l1 and l2:
                if not l1Chosen:
                    nextNode.next = l1
                    l1 = l1.next
                    l1Chosen = True
                else:
                    nextNode.next = l2
                    l2 = l2.next
                    l1Chosen = False
                nextNode = nextNode.next
            nextNode.next = l1 if l1 else l2
            head = newList.next


                
            

        

        
       



        
        
        