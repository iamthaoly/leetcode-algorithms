class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Solution 3: DP Bottom Up

        # dp = [{} for _ in range(len(nums + 1))]
        dp = [defaultdict(int) for _ in range(len(nums)+1)]
        # Base case
        # dp[len(nums + 1)][target] = 1
        dp[0][0] = 1 # 1 way to form sum 0 using 0 numbers

        for i in range(len(nums)):
            for summ, count in dp[i].items():
                dp[i + 1][summ + nums[i]] += count
                dp[i + 1][summ - nums[i]] += count

        return dp[len(nums)][target]

        # cur1 = cur2 = target
        # cur = target
        # for i in range(len(nums), -1, -1):
            # count1 = dp[i + 1][cur + nums[i]]
            # count2 = dp[i + 1][cur - nums[i]]
            # dp[i][cur] = count1 + count2

            # dp[i][cur1] = 0
            # dp[i][cur2] = 0
            # dp[i][cur1] += dp[i + 1].get(cur1, 0)
            # dp[i][cur2] += dp[i + 1].get(cur2, 0)
            # cur1 += nums[i]
            # cur2 -= nums[i]
        #     dp[i][cur] = dp[i + 1].get(cur + nums[i], 0) + dp[i + 1].get(cur - nums[i], 0)
        #     cur = 

        # if dp[0].get(0):
        #     return dp[0][0]

        # return 0
        