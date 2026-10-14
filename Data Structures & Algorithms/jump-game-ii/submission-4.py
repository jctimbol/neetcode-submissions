class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
            
        num_jumps = 1
        max_reachable = nums[0]
        curr_reachable = nums[0]

        for i in range(1, len(nums)):
            if max_reachable >= len(nums)-1:
                break
            if i == max_reachable:
                num_jumps += 1
                max_reachable = max(curr_reachable, i+nums[i])
            else:
                curr_reachable = max(curr_reachable, i+nums[i])
            
        return num_jumps

            
