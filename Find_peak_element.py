class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, h = 0, n-1
        if n == 1:
            return 0
        
        while l <= h:
            mid = l + (h-l)//2
            if (mid==0 and nums[mid] > nums[mid+1]) or (mid == n-1 and nums[mid] > nums[mid-1]) or (nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]):
                return mid
            elif nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                h = mid - 1
        return -1
