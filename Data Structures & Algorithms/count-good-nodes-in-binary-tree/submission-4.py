# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #is node greatest in path from root
        if not root:
            return 0
        
        good = []
        def dfs(root, val):
            if not root:
                return
            if root.val >= val:
                val = root.val
                good.append(root)
            
            dfs(root.left, val)
            dfs(root.right, val)
        
        dfs(root, root.val)

        return len(good)