class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        low=0
        high=len(s1)-1
        d={}
        for i in range(0,len(s1)):
            d[s1[i]]=d.get(s1[i],0)+1
        l={}
        while high<len(s2):
            i=low
            while(i<=high):
                l[s2[i]]=l.get(s2[i],0)+1
                i+=1
            if d==l:
                return True
            else:
                l.clear()
                high=high+1
                low=low+1
        return False