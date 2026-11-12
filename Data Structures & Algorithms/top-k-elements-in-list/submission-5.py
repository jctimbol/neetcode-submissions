class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_counts = sorted(counts, key=counts.get)
        res = []
        for i in range(k):
            res.append(sorted_counts.pop())
        
        return res