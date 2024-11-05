class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## left pointer for keeping all the unique elements and right pointer for scanning for any unique elemnets.
        n = len(nums)
        left, right = 1, 1
        while right < n:
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                right +=1
                left +=1
            else:
                right +=1

        return left
