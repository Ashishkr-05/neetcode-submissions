class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        best=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<best:
                best=prices[i]
            maxprofit=max(maxprofit,prices[i]-best)

        return maxprofit