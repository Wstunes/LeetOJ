__author__ = 'wangshuo'


'''
profit[i] means the max profit in price[0]... price [i]
profit[i+1] = max(profit[i],price[i+1]-minPrice)
'''
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
         if len(prices) <= 1:
             return 0
         profit = prices[1] - prices[0]
         minPrice = prices[0]
         for i in range(len(prices) - 1):

                 minPrice = min(minPrice,prices[i])
                 profit = max(profit,prices[i+1]-minPrice)

         if profit < 0:
             return 0
         return profit


s = Solution()
print s.maxProfit([1,2,4])