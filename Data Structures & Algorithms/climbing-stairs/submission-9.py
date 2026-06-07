class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]

        for i in range(2, n):
            steps.append(steps[i-2]+steps[i-1])
        print(steps)
        return steps[n-1]