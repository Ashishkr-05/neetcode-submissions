class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low=0
        high=0
        maxlength=0
        d={}
        while(high<len(s)):
            if s[high] in d:
                if d[s[high]]>=low:
                    low=d[s[high]]+1
            length=high-low+1
            maxlength=max(maxlength,length)
            d[s[high]]=high
            high=high+1
        return maxlength