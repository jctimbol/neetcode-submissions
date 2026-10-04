class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freqs = {} # num -> frequency
        for num in nums:
            if num not in num_freqs:
                num_freqs[num] = 1
            else:
                num_freqs[num] += 1

        res = []

        for i in range(k):
            max_key = max(num_freqs, key=num_freqs.get)
            res.append(max_key)
            num_freqs.pop(max_key)

        return res


