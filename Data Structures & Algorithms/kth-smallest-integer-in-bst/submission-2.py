# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []
        ans = 0
        def dfs(root, visited, k):
            if not root:
                return None

            left = dfs(root.left, visited, k)
            if left is not None:
                return left

            visited.append(root.val)
            if len(visited) == k:
                return visited[-1]
            
            return dfs(root.right, visited, k)

        return dfs(root, visited, k)