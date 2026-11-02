# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = []

        def dfs(root, greatest):
            if not root:
                return
            if root.val >= greatest:
                good.append(root)
                greatest = root.val
            dfs(root.left, greatest)
            dfs(root.right, greatest)
            
        dfs(root, root.val)
        return len(good)