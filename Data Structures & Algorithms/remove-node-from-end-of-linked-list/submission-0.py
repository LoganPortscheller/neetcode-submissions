# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node = head
        nodes = list()

        # Put all nodes in a List
        while current_node:
            nodes.append(current_node)
            current_node = current_node.next

        nth_node_from_end = nodes[-n]

        if nth_node_from_end == head:
            # Move head right one
            head = nth_node_from_end.next
            return head
        
        nodes[-(n + 1)].next = nth_node_from_end.next
        return head

        