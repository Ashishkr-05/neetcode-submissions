class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        maxlen=0
        maxf=0
        d={}
        while(r<len(s)):
            d[s[r]] = d.get(s[r],0)+1
            maxf=max(d.values())
            if (r-l+1)- maxf > k:
                d[s[l]] = d.get(s[l])-1
                if d[s[l]]==0:
                    del d[s[l]]
                l=l+1
            if (r-l+1)-maxf <= k:
                maxlen=max(maxlen,r-l+1)
            r=r+1
        return maxlen
