class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        best=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>best:
                maxprofit=max(maxprofit,prices[i]-best)
            best=min(best,prices[i])

        return maxprofit