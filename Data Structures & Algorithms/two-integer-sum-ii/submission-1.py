class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,len(numbers)):
            x=target-numbers[i]
            if x in numbers:
                return [i+1,numbers.index(x)+1]
      
