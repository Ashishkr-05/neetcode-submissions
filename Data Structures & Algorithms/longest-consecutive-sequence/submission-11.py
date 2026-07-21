class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest=1
        last_smaller=float('-inf')
        cnt=0
        if len(nums)<=1:
            return len(nums)
        for i in range(0,len(nums)):
            if nums[i]-1==last_smaller:
                last_smaller=nums[i]
                cnt=cnt+1
            elif nums[i]!=last_smaller:
                last_smaller=nums[i]
                cnt=1
            longest=max(longest,cnt)
        return longest