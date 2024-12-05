class Solution(object):
    def maxProfit(self, prices):
        l, h =0, 1
        max_profit = 0
        while h <= len(prices)-1:
            if prices[l] < prices[h]:
                profit = prices[h] - prices[l]
                max_profit = max(max_profit, profit)
                h +=1
            else:
                l = h
                h +=1
        return max_profit
