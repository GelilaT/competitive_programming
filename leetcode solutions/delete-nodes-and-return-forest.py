# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        ans = []
        tbd = set(to_delete)
        def traverse(root):
            
            if not root:
                return None

            root.left = traverse(root.left)
            root.right = traverse(root.right)

            if root.val in tbd:
                if not root.left and not root.right:
                    return None

                else: 
                    if root.left:
                        ans.append(root.left)

                    if root.right:
                        ans.append(root.right)

                    return None

            return root
            

        node = traverse(root)

        if node:
            ans.append(node)
        return ans



