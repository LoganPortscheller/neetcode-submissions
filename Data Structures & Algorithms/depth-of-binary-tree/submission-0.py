import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        frontier = queue.Queue()
        frontier.put((root, 1))

        depth = 0

        while frontier.qsize() != 0:
            node, current_level = frontier.get()
            depth = max(depth, current_level)

            if node.left:
                frontier.put((node.left, current_level + 1))
            if node.right:
                frontier.put((node.right, current_level + 1))

        return depth




        