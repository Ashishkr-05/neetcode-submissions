class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s1={}
        count=0
        while (count<len(nums)):
            if target-nums[count] in s1:
                return [s1[target-nums[count]],count]
            s1[nums[count]]=count
            count=count+1
