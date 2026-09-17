# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        LCA = []

        def dfs(root):
            if not root:
                return
            
            if p.val < root.val and q.val < root.val:
                dfs(root.left)
            elif p.val > root.val and q.val > root.val:
                dfs(root.right)
            else:
                LCA.append(root)
        
        dfs(root)
        print(LCA)
        return LCA[-1]