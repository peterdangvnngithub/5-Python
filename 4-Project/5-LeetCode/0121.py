class Solution(object):
    def MaxProfit(self, prices):
        # Sliding window Algorithm
        """
        min_price = float('inf')
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = max(profit, price - min_price)
            
        return profit
        """
        # Kadane's Algorithm
        max_ending_here = 0
        max_so_far = 0
        
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            max_ending_here = max(diff, max_ending_here + diff)
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
    
lInt = [7,1,5,3,6,4]
solution = Solution()
print(solution.MaxProfit(lInt))