class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        cnt=1
        longest=1
        if len(nums)<=1:
            return len(nums)
        for i in nums:
            s.add(i)
        for i in s:
            if i-1 not in s:
                while(i+1 in s):
                    cnt=cnt+1
                    i=i+1
                longest=max(longest,cnt)
            else:
                cnt=1
        return longest