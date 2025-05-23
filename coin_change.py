"""
# Time Complexity :
- O(amount * n), where n is the number of coins

# Space Complexity :
- O(amount), for the dp array

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
