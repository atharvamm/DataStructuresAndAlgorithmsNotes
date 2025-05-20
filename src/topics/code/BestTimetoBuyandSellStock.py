
from typing import List

class Solution:
    def maxProfitDP(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        def recurse(index = 0,buy = 0):
            if index == len(prices) - 1:
                if buy == 0:
                    return 0
                return prices[len(prices) - 1]
            
            if (index, buy) in profits:
                return profits[(index, buy)]
            
            cur_profit = 0
            if buy == 0:
                cur_profit = max(
                    -prices[index] + recurse(index+1,buy=1),
                    0 + recurse(index+1,buy = 0)
                )
            else:
                cur_profit = max(
                    prices[index],
                    0 + recurse(index+1, buy = 1)
                )
            

            profits[(index,buy)] = cur_profit
            return profits[(index,buy)]

        profits = {}
        recurse(0,0)
        return profits[(0,0)]

    def maxProfitArr(self, prices: List[int]) -> int:
        bp = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):
            max_profit = max(max_profit, prices[i] - bp)
            bp = min(bp,prices[i])
        
        return max_profit
