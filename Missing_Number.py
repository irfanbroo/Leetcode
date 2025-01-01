##Here, we are using the xor operation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor1 = 0
        for i in range(1, n+1):
            xor1 ^=i
        for i in range(n):
            xor1 ^=nums[i]
        return xor1
