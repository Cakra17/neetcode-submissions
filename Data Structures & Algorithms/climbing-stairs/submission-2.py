class Solution:
    def climbStairs(self, n: int) -> int:
        num = [0] * (n + 1)

        def recursive(i, dp):
            if i == 0 or i == 1:
                return 1
            
            if dp[i] != 0:
                return dp[i]
            
            dp[i] = recursive(i-1, dp) + recursive(i-2, dp)
            return dp[i] 

        return recursive(n, num)