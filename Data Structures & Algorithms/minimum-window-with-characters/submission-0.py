class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d={}
        for i in range(0,len(t)):
            d[t[i]]=d.get(t[i],0)+1
        low=0
        high=0
        minlen=10**9
        cnt=0
        start=-1
        while(high<len(s)):
            if d.get(s[high], 0) > 0:
                cnt=cnt+1
            d[s[high]]=d.get(s[high],0)-1
            while(cnt==len(t)):
                if high-low+1<minlen:
                    minlen=high-low+1
                    start=low
                d[s[low]]=d.get(s[low])+1
                if d[s[low]]>0:
                    cnt=cnt-1
                low=low+1
                    
            high=high+1
        s2=""
        if start==-1:
            return ""
        for i in range(start,start+minlen):
            s2=s2+s[i]
        return s2
                
        