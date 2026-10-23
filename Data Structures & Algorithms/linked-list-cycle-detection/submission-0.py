# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_seen = set()
        
        while head:
            if head in nodes_seen:
                # Cycle detected
                return True
            
            nodes_seen.add(head)
            head = head.next

        return False

        