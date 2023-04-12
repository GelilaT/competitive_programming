# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if root == None:
                return ''
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            vale = f'{root.val}'
            if right:
                vale += f'({left})({right})'
            elif left:
                vale += f'({left})'
            return vale
        return dfs(root)