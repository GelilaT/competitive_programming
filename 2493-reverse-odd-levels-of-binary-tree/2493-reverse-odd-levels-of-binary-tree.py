# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([root])
        reverse = False
        while queue:
            length = len(queue)
            arr = []
            for i in range(length):
                cur = queue.popleft()
                if cur.left: 
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

                if reverse:
                    arr.append(cur)
                    if i >= length / 2:
                        arr[i].val, arr[length - 1 - i].val = arr[length - 1 - i].val, arr[i].val
            
            reverse = not reverse

        return root