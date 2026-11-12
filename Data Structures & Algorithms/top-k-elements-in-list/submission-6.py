class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_counts = sorted(counts, key=counts.get)
        
        return sorted_counts[-k:]