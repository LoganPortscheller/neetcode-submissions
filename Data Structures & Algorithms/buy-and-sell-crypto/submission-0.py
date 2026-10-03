class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            # Buy and sell of same day
            return 0
        
        l = 0
        r = 1
        lowest_buying_price = float('inf')
        max_profit = 0

        while r < len(prices):
            # Lowest buying price is min price in prices from indices 0 to l
            lowest_buying_price = min(lowest_buying_price, prices[l])
            # Calculate max profit if we need to sell of day r
            profit = prices[r] - lowest_buying_price

            max_profit = max(max_profit, profit)

            l += 1
            r += 1
            
        return max_profit
                