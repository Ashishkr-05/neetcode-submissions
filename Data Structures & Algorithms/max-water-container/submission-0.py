class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        for i in range(0,len(heights)):
            for j in range(i+1,len(heights)):
                p=min(heights[i],heights[j])*(j-i)
                if max<p:
                    max=p
        return max
                
          