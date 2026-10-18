class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_frequencies = {0: 1}

        running_sum = 0
        res = 0

        for num in nums:
            running_sum += num
            
            to_search = running_sum - k
            if to_search in prefix_frequencies:
                print(to_search)
                res += prefix_frequencies[to_search]
            
            if running_sum not in prefix_frequencies:
                prefix_frequencies[running_sum] = 1
            else:
                prefix_frequencies[running_sum] += 1
        
        print(prefix_frequencies)

        return res
        
