class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low=0
        high=len(numbers)-1
        for i in range(0,len(numbers)):
            j=high
            while(i<j):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
                else:
                    j=j-1
      
