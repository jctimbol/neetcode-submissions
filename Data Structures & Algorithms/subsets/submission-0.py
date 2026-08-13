class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        currentPath = []

        #use index to avoid duplicates
        def backtrack(index, currentPath, res):
            res.append(list(currentPath))
                
            for i in range(index, len(nums)):
                currentPath.append(nums[i])
                backtrack(i+1, currentPath, res)
                currentPath.pop()
        
        backtrack(0, currentPath, res)
        return res
                