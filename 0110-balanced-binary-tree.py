# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance(node):
            if not node:
                return 0

            l, r = balance(node.left), balance(node.right)
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1

            return 1 + max(l, r)

        return balance(root) != -1
