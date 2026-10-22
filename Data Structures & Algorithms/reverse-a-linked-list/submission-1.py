# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        # Reverse linked list for linked list from head.next to the end
        tail = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return tail

        # prev = None
        # next_node = None


        # while head != None:
        #     # Save pointer to next node
        #     next_node = head.next
            
        #     # Point next to previous node
        #     head.next = prev

        #     # Make adjustments for next iteration
        #     prev = head

        #     if not next_node:
        #         return head
        #     else:
        #         head = next_node

        # return head

        



