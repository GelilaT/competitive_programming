# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if not root:
                return []
            else:
                res = traverse(root.left) + [root.val] + traverse(root.right)
                return res
        arr = traverse(root)
        count = Counter(arr)
        max_freq = max(count.values())
        ans=[]
        for k,i in count.items():
            if i == max_freq:
                ans.append(k)
        return ans
