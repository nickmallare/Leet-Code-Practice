
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        currentNode = ListNode()
        result = currentNode
        while l1 and l2:
            if l1.val > l2.val:
                currentNode.next = l2
                l2 = l2.next
            else:
                currentNode.next = l1
                l1 = l1.next
            
            currentNode = currentNode.next

        #handle edge case of just one list having remaining nodes 
        else:
            currentNode.next = l1 or l2
        return result.next

      