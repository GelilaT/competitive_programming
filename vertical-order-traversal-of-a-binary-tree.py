# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        traverse = []
        def dfs(root, row, col):
            if root:
                traverse.append((row, col, root.val))
                dfs(root.left, row + 1, col - 1)
                dfs(root.right, row + 1, col + 1)
            return
        dfs(root, 0, 0)
        traverse = sorted(traverse, key=lambda x:x[1])
        my_dict = defaultdict(list)
        for row, col, val in traverse:
            my_dict[col].append((row, val))
        
        ans = []
        for col in my_dict:
            res = []
            for row, val in sorted(my_dict[col], key=lambda x: (x[0], x[1])):
                res.append(val)
            ans.append(res)
        return ans