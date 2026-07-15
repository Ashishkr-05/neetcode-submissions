class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s1={}
        for i in nums:
            if i in s1:
                s1[i]=s1.get(i)+1
            else:
                s1[i]=s1.get(i,0)+1
        l=[]
        for i in range(0,k):
            key=max(s1,key=s1.get)
            l.append(key)
            s1[key]=0
        l.sort()
        return l