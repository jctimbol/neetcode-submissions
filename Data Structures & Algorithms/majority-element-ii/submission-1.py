class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = math.floor(len(nums)/3)
        counts = Counter(nums)
        res = []
        for key in counts:
            if counts[key] > threshold:
                res.append(key)

                
        return res