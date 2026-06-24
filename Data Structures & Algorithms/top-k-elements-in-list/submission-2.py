class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = []
        num_heap = []
        num_map = dict()
        for num in nums:
            if num not in num_map:
                num_map[num] = 1
            else:
                num_map[num] += 1

        for i in range(0, k):

            key = max(num_map, key=num_map.get)
            elements.append(key)
            num_map.pop(key)
        return elements