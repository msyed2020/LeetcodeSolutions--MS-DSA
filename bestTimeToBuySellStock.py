def maxProfit(self, prices: list[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0
        for _ in range(len(prices)-1):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            else:
                buy = sell
            sell += 1
        return maxProfit

# Add ex
print(maxProfit([1,2,3,4,5]))
print(maxProfit([3,3,3,3,3]))