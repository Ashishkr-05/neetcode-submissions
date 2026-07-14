class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1={}
        s2={}
        if len(s)==len(t):
            for i in s:
                s1[i]=s1.get(i,0)+1
            for i in t:
                s2[i]=s2.get(i,0)+1
            if s1 != s2:
                return False
            else:
                return True
        else:
            return False