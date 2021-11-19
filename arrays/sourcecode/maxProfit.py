from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices):
            start,profit=0,0
            for i in range(1,len(prices)):
                if prices[i]<prices[start]:
                    start=i
                if profit<prices[i]-prices[start]:
                    profit=prices[i]-prices[start]
            return profit
        return 0