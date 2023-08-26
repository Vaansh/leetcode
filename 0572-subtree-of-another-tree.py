# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_subtree(n1, n2):
            if not n1 and not n2:
                return True

            if not n1 or not n2:
                return False

            return (
                n1.val == n2.val
                and is_subtree(n1.left, n2.left)
                and is_subtree(n1.right, n2.right)
            )

        if not root:
            return False

        if root.val == subRoot.val and is_subtree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
