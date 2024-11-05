class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count =nums[0], 1
        n = len(nums) 
        for i in range(1,n):
            if candidate == nums[i]:
                count +=1
            elif count == 0:
                candidate = nums[i]
            else:
                count -=1
        return candidate
        
