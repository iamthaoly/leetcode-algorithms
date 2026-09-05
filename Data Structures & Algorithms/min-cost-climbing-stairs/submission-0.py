class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)

        for i in range(len(cost) - 1, -1, -1):
            r1 = dp[i + 1] if i + 1 < len(cost) else 0
            r2 = dp[i + 2] if i + 2 < len(cost) else 0
            dp[i] = cost[i] + min(r1, r2)

        return min(dp[0], dp[1])