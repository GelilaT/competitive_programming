# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        def construct(root, val):
            if root.val > val:
                if not root.left:
                    root.left = TreeNode(val)
                    return
                construct(root.left, val)
            if root.val < val:
                if not root.right:
                    root.right = TreeNode(val)
                    return
                construct(root.right, val)

        for num in preorder[1:]:
            construct(root, num)
        return root 
