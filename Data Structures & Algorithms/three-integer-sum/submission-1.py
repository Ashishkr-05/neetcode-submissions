class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums.sort()
        for i in range(0,len(nums)):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if sum<0:
                    j+=1
                elif sum>0:
                    k-=1
                else:
                    l.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while (j<k and nums[j]==nums[j-1]):
                        j+=1
        return l
