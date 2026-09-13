# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])

        levels = []

        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            levels.append(level)
        
        ans = []
        for level in levels:
            ans.append(level[-1])

        return ans            

