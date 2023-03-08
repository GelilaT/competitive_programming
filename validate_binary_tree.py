# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inOrder(root):
            if root == None:
                return []
            else:
                return inOrder(root.left) + [root.val] + inOrder(root.right)
           
        result = inOrder(root)
        
        if (all(result[i] < result[i + 1] for i in range(len(result) - 1))):
            return True
        return False
