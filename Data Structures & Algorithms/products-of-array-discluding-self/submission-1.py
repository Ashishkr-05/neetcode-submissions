class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=[0]*n
        prefix=[0]*n
        suffix=[0]*n
        prefix[0]=1
        suffix[len(nums)-1]=1
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        for i in range(0,len(nums)):
            output[i]=prefix[i]*suffix[i]
        return output
