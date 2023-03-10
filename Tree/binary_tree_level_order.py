# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = defaultdict(list)
        if root:
            answer[0] = [root.val]
        def traverse(root,count):
            if not root:
                return
            if root.right and root.left:
                answer[count] += [root.left.val,root.right.val]
            elif root.left:
                answer[count] += [root.left.val]
            elif root.right:
                answer[count] += [root.right.val]
            
            traverse(root.left,count + 1)
            traverse(root.right,count + 1)
        traverse(root,1)
        return answer.values()
