# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        flag = False
        res = []
        def checker(root,target,path):
            if root:
                if not root.left and not root.right:
                    if target - root.val == 0 :
                        path += [root.val]
                        res.append(path.copy())
                    return
                checker(root.left,target - root.val,path + [root.val])
                checker(root.right,target - root.val,path + [root.val])
        checker(root,targetSum,[])
        return res