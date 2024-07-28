# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        elif n == 2 :
            return 2
        elif n == 3 :
            return 3
        
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range( 2 , n + 1 ):
            dp[i] = dp[ i - 1 ] + dp[ i - 2 ]
        return dp[ -1 ]


        
