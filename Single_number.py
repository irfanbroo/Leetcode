class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor1 = nums[0]
        for i in range(1,n):
            xor1 = xor1 ^ nums[i]
        return xor1
