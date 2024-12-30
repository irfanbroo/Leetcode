##This is a hashmap solution


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hnum = {}
       for index, num in enumerate(nums):
            comp = target - num

            if comp in hnum:
                return [hnum[comp], index]
            else:
                hnum[num] = index
        
