class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root == None:
            return None
        if val == root.val:
            return root
        if val > root.val:
            return self.searchBST(root.right,val)
        if val < root.val:
            return self.searchBST(root.left,val)
