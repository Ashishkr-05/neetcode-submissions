class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        low=0
        high=len(nums)-1
        for i in range(0,len(nums)):
            p=1
            for j in range(0,len(nums)):
                if j == i:
                    continue
                else:
                    p=p*nums[j]
            output.append(p)
        return output