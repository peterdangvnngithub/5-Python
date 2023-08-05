class Solution(object):
    def MaxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 10000
        sell = 0
        length = len(prices)
        print("Length: " + str(length))
        for i in range(0, length):
            if prices[i] < buy and i < length - 1:
                buy = prices[i]
                print("Buy: " + str(buy))
                print("Sell: " + str(sell))
                continue
            if prices[i] > sell:
                sell = prices[i]
                print("Buy: " + str(buy))
                print("Sell: " + str(sell))
                continue

        return sell - buy if sell - buy > 0 else 0
    
lInt = [2,1,2,0,1]
solution = Solution()
print(solution.MaxProfit(lInt))