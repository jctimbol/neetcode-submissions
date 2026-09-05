class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, n):
            curr = cost[i]
            cost[i] = min(curr+prev1, curr+prev2)
            prev2 = cost[i-1]
            prev1 = cost[i]
        
        print(cost)
        return min(prev1, prev2)