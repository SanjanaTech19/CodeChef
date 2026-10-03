class Solution:
    def singleNumber(self, nums):
        # write your code here
        
        for i in nums:
            if nums.count(i) == 1:
                return i
        
