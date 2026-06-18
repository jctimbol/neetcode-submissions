class Solution:
    def isHappy(self, n: int) -> bool:
        seen = False
        nums = set()
        n_str = str(n)
        while not seen:
            curr_sum = 0
            for char in n_str:
                curr_sum += (int(char) ** 2)
            
            if curr_sum in nums:
                return False
            elif curr_sum == 1:
                return True
            else:
                nums.add(curr_sum)
                n_str = str(curr_sum)
        return False