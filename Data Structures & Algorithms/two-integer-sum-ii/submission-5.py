class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            remaining = target - numbers[r] - numbers[l]
            if remaining == 0:
                return [l+1, r+1]
            elif remaining > 0:
                l += 1
            else:
                r -= 1
        
        return []