# this might look confusing at first and just think about the property of the array in which where will be the most highest number located  HINT:(its either in the extreme left which is negative number and when its squared its gonan be huge or its in the right side of the array)



class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r =0, len(nums)-1
        ans =[]
        while l <=r:
            if (nums[l] * nums[l]) > (nums[r]*nums[r]):
                ans.append(nums[l] * nums[l])
                l+=1
            else:
                ans.append(nums[r] * nums[r])
                r -=1
        return ans[::-1]
            
