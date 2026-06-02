class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # index -> value
        map = dict()
        i=0
        for num in nums:
            map[num]=i
            i += 1
        
        i=0
        for num in nums:
            diff = target - num;
            if diff in map:
                if(i == map.get(diff)):
                    i += 1
                    continue
                return [i,map.get(diff)]
            i += 1
        return []
