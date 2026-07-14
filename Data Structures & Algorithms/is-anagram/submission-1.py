class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1={}
        s2={}
        if len(s)==len(t):
            for i in s:
                s1.update({i:s.count(i)})
            for j in t:
                s2.update({j:t.count(j)})
            if s1 != s2:
                return False
            else:
                return True
        else:
            return False