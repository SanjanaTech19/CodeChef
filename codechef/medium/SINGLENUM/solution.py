class Solution:
    def singleNumber(self, nums):
        # write your code here
        
        result = 0
        for num in nums:
            result ^= num
        return result
        
