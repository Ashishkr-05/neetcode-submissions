class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""

        for ch in s:
            if ch.isalnum():
                result += ch.lower()
        low=0
        high=len(result)-1
        while(low<=high):
            if result[low]==result[high]:
                low=low+1
                high=high-1
            else:
                return False
        return True