class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        c = 0
        for i in range(n):
            if nums[i]!=val:
                nums[c] = nums[i]
                c+=1
        return c
