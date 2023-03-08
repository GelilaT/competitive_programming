# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(p,q):
            if not p or not q:
                return p == q
            return p.val == q.val and symmetric(p.left,q.right) and symmetric(p.right,q.left)
        return symmetric(root,root)
