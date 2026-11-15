# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bst
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            level = len(q)
            curr_level = []
            for i in range(level):
                curr = q.popleft()
                curr_level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(curr_level)
        
        return res