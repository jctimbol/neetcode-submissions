class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        #dp[x] - minimum coins to make amount x
        for amt in range(1, amount+1): #go from 1 to amount
            for coin in coins:
                if amt >= coin: #can use this coin
                    dp[amt] = min(dp[amt], 1+dp[amt-coin])
        
        return -1 if dp[amount] > amount else dp[amount]