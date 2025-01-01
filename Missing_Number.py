##Here, we are using the xor operator 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor1 = nums[0]
        
        for i in range(1,n):
            xor1 = xor1 ^ nums[i]
        for i in range(n+1):
            xor1 = xor1 ^ i
        return xor1
