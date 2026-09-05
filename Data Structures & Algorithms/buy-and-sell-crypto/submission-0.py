class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input: prices[], prices[i] price on day i
        # 1 <= prices[] length <= 100
        # 0 < prices[i] <= 100

        # buy one day, sell one day
        # output: max profit

        # naive: nested loop
        # 
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
        return max_profit