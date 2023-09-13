# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = set()

        def helper(node):
            if node:
                values.add((node.val))
                helper(node.left)
                helper(node.right)

        helper(root)

        values = list(values)
        values.sort()

        return values[k - 1]
