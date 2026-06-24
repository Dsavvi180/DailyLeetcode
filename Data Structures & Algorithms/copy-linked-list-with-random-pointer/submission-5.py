class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        createdNodes = {}
        
        # Pass 1: Create the clone nodes using unique tuple keys
        tmpNode = head
        while tmpNode:
            tmpNodeRandom = tmpNode.random.val if tmpNode.random else None
            tmpNodeNext = tmpNode.next.val if tmpNode.next else None
            
            # Including 'tmpNode' itself guarantees uniqueness across duplicate values
            tuple_key = (tmpNode, tmpNode.val, tmpNodeNext, tmpNodeRandom)
            createdNodes[tuple_key] = Node(tmpNode.val)
            
            tmpNode = tmpNode.next

        # Safely grab the clone of the head node to return later
        headNext = head.next.val if head.next else None
        headRandom = head.random.val if head.random else None
        newHead = createdNodes.get((head, head.val, headNext, headRandom))
        
        # Pass 2: Wire up the next and random connections
        tmpNode = head
        while tmpNode:
            tmpNodeRandom = tmpNode.random.val if tmpNode.random else None
            tmpNodeNext = tmpNode.next.val if tmpNode.next else None
            
            # Fetch the cloned node currently being processed
            newNode = createdNodes.get((tmpNode, tmpNode.val, tmpNodeNext, tmpNodeRandom))
            
            # Safely build the tuple key for the NEXT node if it exists
            nextTmpNode = tmpNode.next
            if nextTmpNode:
                next_key = (
                    nextTmpNode, 
                    nextTmpNode.val, 
                    nextTmpNode.next.val if nextTmpNode.next else None, 
                    nextTmpNode.random.val if nextTmpNode.random else None
                )
                newNode.next = createdNodes.get(next_key)
            else:
                newNode.next = None
                
            # Safely build the tuple key for the RANDOM node if it exists
            randomTmpNode = tmpNode.random
            if randomTmpNode:
                random_key = (
                    randomTmpNode, 
                    randomTmpNode.val, 
                    randomTmpNode.next.val if randomTmpNode.next else None, 
                    randomTmpNode.random.val if randomTmpNode.random else None
                )
                newNode.random = createdNodes.get(random_key)
            else:
                newNode.random = None
                
            tmpNode = tmpNode.next
        
        return newHead
            
            
        

        