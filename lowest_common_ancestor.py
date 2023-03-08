# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def search(root):

            if not root:
                return False
            else:
                left = search(root.left)
                right = search(root.right) 
                me = False
                if root == p or root == q:
                    me = True
                if me:
                    if left or right:
                        self.ans = root 
                else:
                    if left and right:
                        self.ans = root
                return me or left or right

        search(root)
        
        return self.ans


           
           
