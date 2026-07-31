class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        low=0
        high=k-1
        maxelement=0
        l=[]
        while(high<len(nums)):
            maxelement=nums[low]
            if high-low+1<=k:
                i=low
                while(i<=high):
                    maxelement=max(maxelement,nums[i])
                    i+=1
                l.append(maxelement)
            low+=1
            high+=1
        return l