class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = math.floor(len(nums)/3)
        freqs = {}
        res = []
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
            
            if freqs[num] > threshold and num not in res:
                res.append(num)
        
        return res