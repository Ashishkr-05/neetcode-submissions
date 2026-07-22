class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low=0
        high=len(heights)-1
        max=0
        while(low<high):
            s=min(heights[low],heights[high])*(high-low)
            if max<s:
                max=s
            elif heights[low]<heights[high]:
                    low=low+1
            else:
                    high=high-1
        return max
