class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[] min coins per val up to amount
        # dp[0] -> 0 coins
        # worst case -> 1 * val coins per val
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for amt in range(1, amount+1):
            for coin in coins:
                if amt >= coin: # can use coin
                    dp[amt] = min(dp[amt], 1 + dp[amt-coin])
        
        return -1 if dp[amount] == (amount + 1) else dp[amount]