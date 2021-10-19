# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


#can probably find a faster way to solve this problem
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = None
        while head:
            currentNode = head
            head = head.next
            currentNode.next = answer
            answer = currentNode
        return answer




