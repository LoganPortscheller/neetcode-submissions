# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Invert binary tree treating left child as root
        root.left = self.invertTree(root.left)
        # Invert binary tree treating right child as root
        root.right = self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root
        

        