class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in range(0,len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                l.append(s[i])
            else:
                if not l:
                    return False
                ch=l.pop()
                if (s[i]==")" and ch=="(") or (s[i]=="]" and ch=="[") or (s[i]=="}" and ch=="{") :
                    continue
                else:
                    return False
        return len(l) == 0

